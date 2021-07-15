n = int(input())
rows = [0] * n
cols = [0] * n
for r in range(n):
    s = input()
    for c in range(n):
        if s[c] == "C":
            rows[r] += 1
            cols[c] += 1
ans = 0
for i in range(n):
    ans += rows[i] * (rows[i] - 1) // 2
    ans += cols[i] * (cols[i] - 1) // 2
print(ans)
