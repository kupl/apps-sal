3


def readln():
    return tuple(map(int, input().split()))


(n,) = readln()
t = (-1,) + readln()
v = (0,) + readln()
cnt = [0] * (n + 1)
for i in range(1, n + 1):
    cnt[v[i]] += 1
ans = []
for i in range(1, n + 1):
    if t[i] == 1:
        j = i
        tmp = [i]
        while t[v[j]] == 0 and cnt[v[j]] == 1:
            j = v[j]
            tmp.append(j)
        if len(tmp) > len(ans):
            ans = tmp
print(len(ans))
print(*tuple(reversed(ans)))
