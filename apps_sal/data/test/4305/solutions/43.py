h, a = map(int, input().split())
ans = 0

while(h > 0):
    ans += 1
    h = h - a

print(ans)
