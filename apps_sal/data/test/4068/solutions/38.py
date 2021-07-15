n, m = map(int,input().split())
broken = set()
stairs = [0]*(n+2)
stairs[n] = 1

for _ in range(m):
    a = int(input())
    broken.add(a)

for j in range(n):
    if n-1-j in broken:
        continue
    stairs[n-1-j] = stairs[n-j]+stairs[n+1-j]

print(stairs[0]%1000000007)
