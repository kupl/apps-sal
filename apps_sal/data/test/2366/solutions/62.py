n = (int)(input())
a = input().split()
for i in range(n):
    a[i] = (int)(a[i])

dic = {}
sum = 0
for i in range(n):
    if not a[i] in dic:
        dic[a[i]] = 1
    else:
        dic[a[i]] += 1
        sum += dic[a[i]] - 1

for i in a:
    print((sum - dic[i] + 1))
