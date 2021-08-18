def intput(): return [int(i) for i in input().split()]


n = int(input())
l = sorted([intput() for i in range(n)])
i = res = 0
while i < n:
    k = l[i][1]
    while i < n and k >= l[i][0]:
        i += 1
        if i < n and k > l[i][1]:
            k = l[i][1]
    res += 1
print(res)
