# alpha = "abcdefghijklmnopqrstuvwxyz"
# prime = 998244353 
INF = 1000_000_000

# from heapq import heappush, heappop
# from collections import defaultdict
# from math import sqrt
# from collections import deque      
    
t = 1#int(input())

for test in range(t):
    n = int(input())
    # n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    if n==1:
        print(max(arr[0], -arr[0]-1))
    else:
        for i in range(n):
            if arr[i]>=0:
                arr[i] = -arr[i]-1
        if n%2==1:
            minval = INF
            ind = -1
            for i in range(n):
                if arr[i]<minval:
                    minval = arr[i]
                    ind = i
            arr[ind] = -arr[ind]-1
        print(*arr)

