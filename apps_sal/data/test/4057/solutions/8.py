n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in a:
    if(i in d):
        d[i] += 1
    else:
        d[i] = 1
maxi = 0
for i in d:
    maxi = max(maxi, d[i])
print(maxi)
