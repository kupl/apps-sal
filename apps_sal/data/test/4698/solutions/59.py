n = int(input())
t = list(map(int, input().split()))
for _ in range(int(input())):
    (p, x) = map(int, input().split())
    ans = 0
    for i in range(n):
        if p - 1 == i:
            ans += x
        else:
            ans += t[i]
    print(ans)
