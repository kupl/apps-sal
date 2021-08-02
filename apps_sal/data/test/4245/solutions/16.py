A, B = map(int, input().split())
p = 1
ans = 0
while(p < B):
    p += A - 1
    ans += 1
print(ans)
