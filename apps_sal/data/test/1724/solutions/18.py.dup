n = int(input())
a = list(map(int, input().split()))
s = input()

ans = 0
sm = 0

for i in range(n):
    if s[i] == '1':
        ans = max(ans + a[i], sm)
    sm += a[i]

print(ans)
