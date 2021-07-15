a, b = list(map(int, input().split()))
n = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
for c in input():
    n[c] += 1

ans = 0
for i in sorted(list(n.values()), reverse=True):
    x = min(i, b)
    ans += x * x
    b -= x
    if not b:
        break

print(ans)

