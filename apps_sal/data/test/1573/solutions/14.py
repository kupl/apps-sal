n, m = list(map(int, input().split()))
matrix = []
ans = -1000000
kol = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    matrix.append((a, b))
matrix.sort()
pr = [0]
for i in range(n):
    pr.append(matrix[i][1] + pr[-1])
for i in range(n):
    kol = 0
    s = matrix[i][1]
    cost = matrix[i][0]
    l = i
    r = n
    while l + 1 < r:
        mi = (l + r) // 2
        if matrix[mi][0] - cost < m:
            l = mi
        else:
            r = mi

    ans = max(ans, pr[l + 1] - pr[i])
print(ans)    
        

