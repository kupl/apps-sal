N, A, B = list(map(int, input().split()))
ans = 0
for x in range(1, N + 1):
    y = sum(int(c) for c in str(x))
    if A <= y and y <= B:
        ans += x
print(ans)
