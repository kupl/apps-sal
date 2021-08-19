N = int(input())
a = sorted([int(c) for c in input().split()])
# 2回の変わり目を記憶
c1, c2, c3 = [0, 0, 0]
ma = 1
for i in range(N):
    if i > 0:
        if a[i] == a[i - 1] + 1:
            c1 = c2
            c2 = c3
            c3 = i
        elif a[i] != a[i - 1]:
            c1, c2, c3 = [i, i, i]
    if ma < i - c1 + 1:
        ma = i - c1 + 1

print(ma)
