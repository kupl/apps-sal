X = int(input())
b = 2
p = 2
ans = 1
for b in range(1, X + 1):
    for p in range(2, X + 1):
        beki = b ** p
        if beki <= X:
            ans = max(ans, beki)
        else:
            break
print(ans)
