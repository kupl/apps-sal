(a, b, c) = list(map(int, input().split()))
m = int(input())
USB = []
PS = []
i2 = 0
i1 = 0
ans1 = 0
ans2 = 0
for i in range(m):
    (n, k) = input().split()
    if k == 'USB':
        USB.append(int(n))
    else:
        PS.append(int(n))
USB.sort()
PS.sort()
for i in range(a):
    if i >= len(USB):
        break
    ans1 += USB[i]
    ans2 += 1
    i1 = i + 1
for i in range(b):
    if i >= len(PS):
        break
    ans1 += PS[i]
    ans2 += 1
    i2 = i + 1
for i in range(c):
    if i2 < len(PS) and i1 < len(USB):
        if PS[i2] < USB[i1]:
            ans1 += PS[i2]
            i2 += 1
            ans2 += 1
        else:
            ans1 += USB[i1]
            i1 += 1
            ans2 += 1
    elif i2 >= len(PS):
        if i1 < len(USB):
            ans1 += USB[i1]
            i1 += 1
            ans2 += 1
    elif i1 >= len(USB):
        if i2 < len(PS):
            ans1 += PS[i2]
            i2 += 1
            ans2 += 1
print(ans2, ans1)
