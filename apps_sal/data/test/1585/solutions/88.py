x, y = map(int, input().split())

ans = 0
num = x
while num <= y:
    num *= 2
    ans += 1

print(ans)
