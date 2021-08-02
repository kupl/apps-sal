n = int(input())
l = list(map(int, input().split()))
ls = []
for i in range(n):
    x = 0
    if l[i] >= 0:
        x = int(l[i]**0.5)
    if l[i] != x * x or l[i] < 0:
        ls.append(l[i])
ls.sort()
print(ls[-1])
