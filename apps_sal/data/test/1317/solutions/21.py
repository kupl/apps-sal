from operator import itemgetter
# int(input())
# map(int,input().split())
#[list(map(int,input().split())) for i in range(q)]
#print("YES" * ans + "NO" * (1-ans))
n, m = list(map(int, input().split()))
ai = [0] * m
for i in range(m):
    ai[i * i % m] += 1
ai2 = [0] * m
n3 = n % m
for i in range(1, n3 + 1):
    ai2[i * i % m] += 1
n2 = n // m

ans = 0
for i in range(m):
    i2 = (m - i) % m
    ans += ((ai[i] * n2 + ai2[i]) * (ai[i2] * n2 + ai2[i2]))
print(ans)
