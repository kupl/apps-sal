n, x = list(map(int, input().split()))

ans = 0
for i in range(n):
    inp = input().split(' ')
    if inp[0] == '+':
        x += int(inp[1])
    else:
        if x >= int(inp[1]):
            x -= int(inp[1])
        else:
            ans += 1

print(x, ans)
