n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
sm = sum(a)
mul = sum((i ** 2 for i in a))
ans = (sm ** 2 - mul) // 2 % mod
print(ans)
