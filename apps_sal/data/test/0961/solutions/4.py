#!/usr/bin/pypy3

import cProfile
from sys import stdin,stderr
from heapq import heappush,heappop
from random import randrange

def readInts(): return map(int,stdin.readline().strip().split())
def print_err(*args,**kwargs): print(*args,file=stderr,**kwargs)

def create_heap(ns):
    mins = {}
    maxs = {}
    for i,v in enumerate(ns):
        if v not in mins: mins[v] = i
        maxs[v] = i
    ranges = {}
    rheap = []
    for v,minix in mins.items():
        maxix = maxs[v]
        ranges[v] = (minix,maxix)
        heappush(rheap,(maxix-minix+1,minix))        
    return (ranges,rheap)

def create_heap2(ns):
    mins = {}
    maxs = {}
    for i,v in enumerate(ns):
        if v not in mins: mins[v] = i
        maxs[v] = i
    ranges = {}
    rheap = []
    for v,minix in mins.items():
        maxix = maxs[v]
        ranges[v] = (minix,maxix)
        heappush(rheap,(maxix-minix+1,minix,set([v])))        
    return (ranges,rheap)

def solve(n,ns):
    ranges,pq = create_heap(ns)
    resolved_ranges = {}
    while pq:
        w,lo_ix = heappop(pq)
        #print(len(pq),w,lo_ix)
        if lo_ix in resolved_ranges:
            #print(len(pq))
            continue
        tot_subs = 0
        tot_x = 0
        ix = lo_ix
        fail = False
        xsv = set()
        while ix < lo_ix+w:
            v = ns[ix]
            lo2,hi2 = ranges[v]
            if lo2 < lo_ix or hi2 > lo_ix+w-1:
                lo2 = min(lo2,lo_ix)
                hi2 = max(hi2,lo_ix+w-1)
                heappush(pq, (hi2-lo2+1,lo2) )
                fail = True
                break
            if ix in resolved_ranges:
                rhi_ix,c,x = resolved_ranges[ix]
                tot_x ^= x
                tot_subs += c
                ix = rhi_ix + 1
                continue
            if v not in xsv:
                xsv.add(v)
                tot_x ^= v
            ix += 1
        if not fail:
            resolved_ranges[lo_ix] = (lo_ix+w-1,max(tot_x,tot_subs),tot_x)
    ix = 0
    tot_c = 0
    while ix < n:
        rhi,c,_ = resolved_ranges[ix]
        ix = rhi+1
        tot_c += c
    return tot_c


def solve2(n,ns):
    ranges,pq = create_heap(ns)
    resolved_ranges = {}
    while pq:
        w,lo_ix,xs = heappop(pq)
        print(len(pq),w,lo_ix,xs)
        if lo_ix in resolved_ranges:
            print(len(pq))
            continue
        tot_subs = 0
        tot_x = 0
        for x in xs: tot_x ^= x
        ix = lo_ix
        fail = False
        while ix < lo_ix+w:
            v = ns[ix]
            if v in xs:
                ix += 1
                continue
            if ix in resolved_ranges:
                rhi_ix,c,x = resolved_ranges[ix]
                tot_x ^= x
                tot_subs += c
                ix = rhi_ix + 1
                continue
            lo2,hi2 = ranges[v]
            lo2 = min(lo2,lo_ix)
            hi2 = max(hi2,lo_ix+w-1)
            xs.add(v)
            heappush(pq, (hi2-lo2+1,lo2,xs) )
            fail = True
            break
        if not fail:
            resolved_ranges[lo_ix] = (lo_ix+w-1,max(tot_x,tot_subs),tot_x)
    ix = 0
    tot_c = 0
    while ix < n:
        rhi,c,_ = resolved_ranges[ix]
        ix = rhi+1
        tot_c += c
    return tot_c

def test():
    n = 5000
    ns = []
    for _ in range(n):
        ns.append(randrange(1,n//2))
    print(solve(n,ns))
    
def run():
    n, = readInts()
    ns = list(readInts())
    print(solve(n,ns))
        
run()

