n = int(input())
C = list(input())

a, b = 0, 0
for i in range(n):
    if C[i] == "R":
        a += 1
    ans = max(a, b)

for i in range(n):
    if C[i] == "R":
        a -= 1
    else:
        b += 1
    tmp = max(a, b)
    ans = min(ans, tmp)

print(ans)
