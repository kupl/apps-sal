T = int(input())
for _ in range(T):
    s, n, m = list(map(int, input().split()))
    for i in range(n):
        if ((s // 2) + 10) < s:
            s = s // 2 + 10
    if s <= m * 10:
        print("YES")
    else:
        print("NO")
