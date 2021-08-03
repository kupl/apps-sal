n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
b = sum(a)
c = sum([i * i for i in a])
ans = ((b**2 - c) // 2) % mod
print(ans)
