N = int(input())
WS = [int(i) for i in input().split()]

m = float('inf')
for i in range(N):
    m = min(m, abs(sum(WS[:i]) - sum(WS[i:])))

print(m)
