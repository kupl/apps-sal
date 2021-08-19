n = int(input())
a = list(map(int, input().split()))
sa = sorted(a, reverse=True)
al = 0
bo = 0
for i in range(n):
    if i % 2 == 0:
        al += sa[i]
    else:
        bo += sa[i]
print(al - bo)
