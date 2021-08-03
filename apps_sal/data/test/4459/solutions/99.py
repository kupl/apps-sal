n = int(input())
a = [int(x) for x in input().split()]
a.sort()
flag = [False] * n
res = 0

for i in range(n):
    if flag[i]:
        continue

    c = 0
    j = i

    while a[i] == a[j]:
        c += 1
        flag[j] = True
        j += 1
        if j == n:
            break

    if c == a[i] or c == 0:
        continue
    elif c < a[i]:
        res += c
    else:
        res += c - a[i]

print(res)
