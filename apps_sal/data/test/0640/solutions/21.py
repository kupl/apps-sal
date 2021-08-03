

a, b = list(map(int, input().split()))
ans1 = ans2 = ans3 = 0
for i in range(6):
    if abs(a - (i + 1)) == abs(b - (i + 1)):
        ans1 += 1
    elif abs(a - (i + 1)) < abs(b - (i + 1)):
        ans2 += 1
    else:
        ans3 += 1
print(ans2, ans1, ans3)
