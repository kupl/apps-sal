n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for k in range(4):
    t = [-1] * n
    t[0] = k
    x = False
    for i in range(1, n):
        x = False
        for j in range(4):
            if a[i - 1] == (j | t[i - 1]) and b[i - 1] == (j & t[i - 1]):
                t[i] = j
                x = True
        if not x:
            break
    if x:
        print("YES")
        print(*t)
        return
print("NO")
