n = int(input())
k = int(input())
dis = 1
for i in range(n):
    if dis * 2 <= dis + k:
        dis *= 2
    else:
        dis += k
print(dis)
