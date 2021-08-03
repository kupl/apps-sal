a, b, c = list(map(int, input().split()))
D = (b * b - 4 * a * c) ** 0.5
ans1 = (-b + D) / (2 * a)
ans2 = (-b - D) / (2 * a)
if ans1 < ans2:
    ans1, ans2 = ans2, ans1
print(ans1)
print(ans2)
