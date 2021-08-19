(n, m) = map(int, input().split())
k = [list(map(int, input().split())) for i in range(n)]
c = 0
for i in range(1, m + 1):
    for j in range(n):
        if i not in k[j][1:]:
            break
    else:
        c += 1
print(c)
