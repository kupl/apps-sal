#!/usr/bin/env python3
import sys
import heapq

def minus(n):
    return -n

def solve(N: int, a: "List[int]"):
    ## N+iまでのリストの大きい順のNコのわ  
    left_sum = [0]*(N+1)
    heap = a[:N]
    left_sum[0] = sum(heap)
    heapq.heapify(heap)
    for i in range(N,2*N):
        heapq.heappush(heap,a[i])
        min_value = heapq.heappop(heap)
        left_sum[i-(N-1)]=left_sum[i-N]+a[i]-min_value

    b = list(map(minus,reversed(a)))
    right_sum= [0]*(N+1)
    r_heap = b[:N]
    right_sum[0] = -sum(r_heap)
    heapq.heapify(r_heap)
    for i in range(N,2*N):
        heapq.heappush(r_heap,b[i])
        min_value = heapq.heappop(r_heap)
        right_sum[i-(N-1)]=right_sum[i-N]+(-b[i])-(-min_value)
    
    answer = -10**15
    for j in range(N+1):
        answer = max(answer,left_sum[j]-right_sum[N-j])
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(3 * N)]  # type: "List[int]"
    solve(N, a)

def __starting_point():
    main()

__starting_point()
