from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
z = defaultdict(list)
temp1 = []
temp2 = []
for i in range(n):
    z[a[i]] = i + 1
    temp1.append(a[i])
s = input()
temp1.sort(reverse=True)
for i in s:
    if i == '0':
        x = temp1.pop()
        print(z[x], end=' ')
        temp2.append(x)
    else:
        print(z[temp2.pop()], end=' ')
