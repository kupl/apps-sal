
t = int(input())
for _ in range(t):
    a = input()
    b = input()
    c = input()
    n = len(a)
    flag = True
    for i in range(n):
        if a[i] == c[i] or b[i] == c[i]:
            continue
        flag = False
    if flag:
        print("YES")
    else:
        print("NO")
