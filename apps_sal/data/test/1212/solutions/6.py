3


def readln(): return tuple(map(int, input().split()))


n, k = readln()
h = readln()
ans = s = sum(h[:k])
j = 1
for _ in range(k, n):
    s += -h[_ - k] + h[_]
    if ans > s:
        ans = s
        j = _ - k + 2
print(j)
