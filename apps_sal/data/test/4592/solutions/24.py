N = int(input())
l = [0] * 1000


def divisor_enu(N):
    l = []
    for i in range(2, int(N**0.5) + 1):
        cnt = 0
        if N % i == 0:
            while N % i == 0:
                cnt += 1
                N //= i
            l.append((i, cnt))
    if N != 1:
        l.append((N, 1))
    return l


for i in range(1, N + 1):
    s = divisor_enu(i)
    for j in s:
        l[j[0]] += j[1]
ans = 1
mod = 10**9 + 7
for i in l:
    if 0 < i:
        ans = ans * (i + 1) % mod
print(ans)
