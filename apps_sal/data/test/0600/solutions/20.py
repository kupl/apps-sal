a = int(input())
b = int(input())
ans = 0
for i in range(1, abs(b - a) // 2 + 1):
    ans += 2 * i
if abs(a - b) % 2 != 0:
    ans += abs(b - a) // 2 + 1
print(ans)
