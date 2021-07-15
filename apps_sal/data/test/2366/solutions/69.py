n = int(input())
A = list(map(int, input().split()))
cnt = [0]*n


def choose2(m):
    return m*(m-1)/2


for i in range(n):
    A[i] -= 1

for i in range(n):
    cnt[A[i]] += 1

tot = 0
for i in range(n):
    tot += choose2(cnt[i])

for i in range(n):
    ans = tot
    ans -= choose2(cnt[A[i]])
    ans += choose2(cnt[A[i]]-1)
    print((int(ans)))

