n = int(input())
key = []
ans = 0
for _ in range(n):
    s = int(input())
    if s not in key:
        key.append(s)
        ans += 1
print(ans)
