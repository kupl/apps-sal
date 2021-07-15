n = int(input())
x = list(map(int,input().split()))

ans = float("inf")
for p in range(1,101):
    hp = 0
    for i in x:
        hp += (i-p)**2
    ans = min(ans, hp)
print(ans)
