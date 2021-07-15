t = int(input())
for _ in range(t):
    n = int(input())
    if (n // 2) % 2:
        print("NO")
        continue
    a = []
    s = 0
    for i in range(n // 2):
        s += 2*(i + 1)
        a.append(2*(i + 1))
    for j in range(n // 2 - 1):
        s -= 2*j + 1
        a.append(2*j + 1)
    a.append(s)
    print("YES")
    print(*a)


# a = list(map(int,input().split()))
# n,m = map(int,input().split())


