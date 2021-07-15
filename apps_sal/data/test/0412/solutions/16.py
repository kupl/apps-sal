from math import *
n = int(input())
data = list(map(int, input().split()))
ans = []
for i in range(100):
    help = [2 ** i, 0]
    for j in range(n):
        if data[j] % (2 ** i) == 0:
            help[1] += 1
    ans.append(help)
ans.sort()
index = 0
while ans[index][1]:
    index += 1
index -= 1
print(*ans[index])
