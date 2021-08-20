n = int(input())
ans1 = 1
for i in range(5):
    ans1 *= n + 4 - i
for i in range(1, 6):
    ans1 //= i
ans2 = 1
for i in range(3):
    ans2 *= n + 2 - i
for i in range(1, 4):
    ans2 //= i
print(ans1 * ans2)
