n = int(input())
q = [["-"] * n for _ in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        q[i][x - 1] = False if y == 0 else True
ans = 0
for bit in range(1 << n):
    arr = [False] * n
    for i in range(n):
        if bit >> i & 1 == 1:
            arr[i] = True
    flag = True
    for i in range(n):
        if arr[i] == False:
            continue
        for j in range(n):
            if q[i][j] == "-":
                continue
            if q[i][j] != arr[j]:
                flag = False
                break
    if flag:
        ans = max(ans, arr.count(True))
print(ans)
