n = int(input())
pos = []
neg = []
res = 0
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if a > b:
        pos.append([a, b])
    elif a < b:
        neg.append([a, b])
    else:
        res += (n - 1) * a
pos.sort(key=lambda l: -abs(l[0] - l[1]))
neg.sort(key=lambda l: -abs(l[0] - l[1]))


def f(i, l):
    return l[0] * (i - 1) + l[1] * (n - i)


for i in range(len(pos)):
    res += f(i + 1, pos[i])
for i in range(len(neg)):
    res += f(n - i, neg[i])
print(res)
