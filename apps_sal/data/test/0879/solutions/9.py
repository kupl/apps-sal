from collections import defaultdict
n = int(input())
l = list(map(int, input().split()))
d = defaultdict(int)

for i in range(2, n + 1):
    d[i] = l[i - 2]

x = n
ans = []
while(x != 1):
    ans.append(x)
    x = d[x]
ans.append(1)
for i in ans[::-1]:
    print(i, end=' ')
