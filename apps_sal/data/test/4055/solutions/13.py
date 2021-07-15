n = int(input())
l = [*map(int, input().split())]
res = 0
for i in range(2, n):
    if l[i]:
        if l[i - 2] == l[i] and l[i - 1] == 0:
            l[i] = 0
            res += 1
print(res)
