import math
n = int(input())
a = list(map(int, input().split()))
su = sum(a)
su = math.ceil(su / 2)
c = 0
for i in range(len(a)):
    c += a[i]
    if c >= su:
        print(i + 1)
        break
