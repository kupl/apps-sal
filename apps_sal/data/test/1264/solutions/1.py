n = int(input())
l = list(map(int, input().split()))
m = -1
for i in range(n):
    for j in range(i, n):
        c = 0
        for ind in range(n):
            if i <= ind <= j:
                if l[ind] == 0:
                    c += 1
            else:
                if l[ind] == 1:
                    c += 1
        m = max(m, c)
print(m)
