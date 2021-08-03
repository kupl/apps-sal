n = int(input())
d = {'T': 4, 'C': 6, 'O': 8, 'D': 12, 'I': 20}
ans = 0
for _ in range(n):
    ans += d[input()[0]]
print(ans)
