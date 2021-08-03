x, y = map(int, input().split())

n = [0, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]

if n[x] == n[y]:
    ans = "Yes"
else:
    ans = "No"

print(ans)
