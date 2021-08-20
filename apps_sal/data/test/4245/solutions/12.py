(A, B) = map(int, input().split())
ans = 0
while ans * (A - 1) + 1 < B:
    ans += 1
print(ans)
