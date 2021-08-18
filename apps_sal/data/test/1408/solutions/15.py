n = int(input())
dif = []
li1 = []
li2 = []
a1 = b1 = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    if a == 1:
        li1.append(b)
    else:
        li2.append(b)
li1.sort(reverse=True)
li2.sort(reverse=True)
l1 = len(li1)
l2 = len(li2)
ans = 10000000000
for i in range(l1 + 1):
    for j in range(l2 + 1):
        s = 0
        for k in range(i, l1):
            s += li1[k]
        for k in range(j, l2):
            s += li2[k]
        if i + 2 * j >= s:
            ans = min(ans, i + 2 * j)
print(ans)
