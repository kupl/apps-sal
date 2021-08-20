(x, n) = list(map(int, input().split()))
p = list(map(int, input().split()))
if n:
    l = [0 for _ in range(102)]
    for i in p:
        l[i] = 1
    for i in range(101):
        if l[x - i] == 0:
            ans = x - i
            break
        if l[x + i] == 0:
            ans = x + i
            break
    print(ans)
else:
    print(x)
