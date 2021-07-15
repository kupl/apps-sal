A, B = map(int, input().split())
ans = 0
res = 1

while res < B:
    res += A - 1
    ans += 1

print(ans)
