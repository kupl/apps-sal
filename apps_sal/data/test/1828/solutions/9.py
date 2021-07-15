#!/usr/bin/env python3

read_ints = lambda : list(map(int, input().split()))

def solve(ps):
    ans = 0
    for i in range(len(ps)-2):
        if ccw(ps[i], ps[i+1], ps[i+2]):
            ans += 1
    return ans

def ccw(p1, p2, p3):
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p2[1] - p1[1])*(p3[0] - p1[0]) > 0

def __starting_point():
    n = int(input())
    ps = []
    for i in range(n+1):
        ps.append(read_ints())
    print(solve(ps))

__starting_point()
