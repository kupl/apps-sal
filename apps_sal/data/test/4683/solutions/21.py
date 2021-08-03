n = int(input())
alst = list(map(int, input().split()))
mod = 10**9 + 7

lst_sm = sum(alst)
sm = lst_sm**2
for i in range(n):
    sm -= alst[i]**2
sm //= 2
print((sm % mod))
