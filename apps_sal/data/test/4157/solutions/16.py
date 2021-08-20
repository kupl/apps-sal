n = int(input())
a = input().split()
ans = []
for i in range(n):
    a[i] = int(a[i])
a.sort()
j = 0
while len(a) > 0:
    temp = []
    i = 0
    while i < len(a):
        if a[i] % 3 != 0:
            temp.append(a[i] * pow(3, j))
            a.remove(a[i])
        else:
            a[i] //= 3
            i += 1
    j += 1
    ans.append(temp)
k = len(ans)
for i in range(k):
    for j in range(len(ans[k - i - 1])):
        print(ans[k - i - 1][j], end=' ')
