import sys
n = int(input())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
res = [0] * n
for i in range(n):
    res[i] = n - l[i] - r[i]
for i in range(n):
    ok = 0
    for j in range(i):
        if res[j] > res[i]:
            ok += 1
    if ok != l[i]:
        print("NO")
        return
    ok = 0
    for j in range(i + 1, n):
        if res[j] > res[i]:
            ok += 1
    if ok != r[i]:
        print("NO")
        return
print("YES")
print(' '.join(map(str, res)))
