(a, b) = input().split()
ans = 'z' * 100
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[:i] + b[:j] < ans:
            ans = a[:i] + b[:j]
print(ans)
