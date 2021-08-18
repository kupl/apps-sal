import collections


def fact(N):
    arr = []
    i = 2
    while i * i <= N:
        if N % i == 0:
            while N % i == 0:
                arr.append(i)
                N //= i
        i += 1
    if N > 1:
        arr.append(N)
    return arr


N = int(input())
arr = []
for i in range(1, N + 1):
    arr += fact(i)
arc = collections.Counter(arr)
num74cnt = 0
num24cnt = 0
num14cnt = 0
num4cnt = 0
num2cnt = 0
for val in list(arc.values()):
    if val >= 74:
        num74cnt += 1
    if val >= 24:
        num24cnt += 1
    if val >= 14:
        num14cnt += 1
    if val >= 4:
        num4cnt += 1
    if val >= 2:
        num2cnt += 1
ans = num74cnt
ans += num24cnt * (num2cnt - 1)
ans += num14cnt * (num4cnt - 1)
ans += num4cnt * (num4cnt - 1) // 2 * (num2cnt - 2)

print(ans)
