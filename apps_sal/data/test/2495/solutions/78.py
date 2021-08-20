n = int(input())
A = list(map(int, input().split()))
s1 = 0
now = 0
for i in range(n):
    now += A[i]
    if i % 2 == 1 and now <= 0:
        s1 += 1 - now
        now = 1
    if i % 2 == 0 and now >= 0:
        s1 += now + 1
        now = -1
s2 = 0
now = 0
for i in range(n):
    now += A[i]
    if i % 2 == 0 and now <= 0:
        s2 += 1 - now
        now = 1
    if i % 2 == 1 and now >= 0:
        s2 += now + 1
        now = -1
print(min(s1, s2))
