n = int(input())
d = 1
ans1 = ans2 = 0
for i in range(n, n + 5):
    d *= i
ans1 = d // 120
d = 1
for i in range(n, n + 3):
    d *= i
ans2 = d // 6
print(ans1 * ans2)
