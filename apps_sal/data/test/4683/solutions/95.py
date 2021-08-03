n = int(input())
a = list(map(int, input().split()))
a.sort()
s = sum(a)
x = [i**2 for i in a]
x = sum(x)
ans = (s**2 - x) // 2
mod = 10**9 + 7
print(ans % mod)
