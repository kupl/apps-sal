import math


def calc(num, list1, list2):
    s = 0
    for i in range(num):
        s += (list1[i] - list2[i]) ** 2
    d = math.sqrt(s)
    return d


N, D = map(int, input().split())
L = []
ans = 0

for i in range(N):
    L.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i + 1, N):
        c = calc(D, L[i], L[j])
        if c.is_integer():
            ans += 1

print(ans)
