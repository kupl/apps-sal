a = int(input())
b = int(input())
s = 1
ans = 0
for i in range(abs(b - a) // 2):
    ans += s * 2
    s += 1
if abs(b - a) % 2 == 1:
    ans += s
print(ans)
