#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import heapq

def main():
    n = int(input())
    values=[]
    heap_values=[]
    values=list(map(int,input().split()))
    [heapq.heappush(heap_values, value) for value in values]

    while len(heap_values)!=1:
        tmp1=heapq.heappop(heap_values)
        tmp2=heapq.heappop(heap_values)
        tmp_value=(tmp1+tmp2)/2
        heapq.heappush(heap_values,tmp_value)

    print(heap_values[0])

def __starting_point():
    main()
__starting_point()
