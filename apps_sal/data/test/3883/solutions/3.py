x, y = [int(x) for x in input().split()]
n1 = x + y
ans1 = -1
ans2 = -1
if n1 // y - (n1 // y % 2) != 0:
    ans1 = n1 / (n1 // y - (n1 // y % 2))
n2 = x + y
if n2 // y - (n2 // y % 2) != 0:
    ans2 = n2 / (n2 // y - (n2 // y % 2))
print(min(ans1, ans2))
