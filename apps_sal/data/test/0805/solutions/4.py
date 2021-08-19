n = int(input())
a1 = list()
for i in range(0, 101):
    a1.insert(i, 0)
#	print(a1[i])
for i in range(0, n):
    a, b = list(map(int, input().split()))
    # print(i)
    if i != 0:
        for j in range(a, b):
            # print(j)
            a1[j] = 1
            # print(a1[j])
    else:
        l = a
        r = b
ans = 0
for i in range(l, r):
    # print(i)
    if a1[i] == 0:
        ans = ans + 1
print(ans)
