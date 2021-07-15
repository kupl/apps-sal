n = int(input())
li = list(map(int, input().split()))
mod = 10**9 + 7
sm = sum(li)
mul = sum([i**2 for i in li])
ans = ((sm ** 2 - mul) // 2) % mod
print(ans)

