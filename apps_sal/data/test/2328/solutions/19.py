import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    aa = list(map(int, input().split()))
    best = 10000000000
    for i in range(n-k):
        if aa[i+k] - aa[i] < best:
            best = aa[i+k] - aa[i]
            bestpos = i
    print(aa[bestpos] + best//2)
