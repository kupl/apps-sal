a = list(input())
b = list(input())

ans = 0
for p, q in zip(a, b):
    if p != q:
        ans += 1
print(ans)
