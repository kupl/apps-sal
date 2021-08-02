z = list(map(int, input().split()))
n = z[0]
inp = list(input())
out = list(input())
ans = 0
for i in range(n):
    if abs(int(inp[i]) - int(out[i])) > 5:
        ans += 10 - abs(int(inp[i]) - int(out[i]))
    else:
        ans += abs(int(inp[i]) - int(out[i]))

print(ans)
