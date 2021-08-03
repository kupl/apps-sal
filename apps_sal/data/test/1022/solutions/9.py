def lr(a):
    l = [0] * len(a)
    r = [0] * len(a)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[j] > a[i]:
                r[i] += 1
            if a[i] > a[j]:
                l[j] += 1
    return l, r


n = int(input())
l = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]
a = [0] * n
for i in range(n):
    for j in range(n):
        if l[j] + r[j] == i:
            a[j] = n - i
l1, r1 = lr(a)
if l1 != l or r1 != r:
    print("NO")
else:
    print("YES")
    print(' '.join([str(i) for i in a]))
