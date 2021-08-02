r = input()
l = len(r)
ans1 = 0
prev = r[0]
ans2 = 1
for i in range(1, l):
    if (r[i] != prev):
        ans2 = ans2 + 1
    else:
        ans1 = max(ans1, ans2)
        ans2 = 1
    prev = r[i]
ans1 = max(ans1, ans2)
ans3 = 1
prev = r[0]
for i in range(1, l):
    if (r[i] == prev):
        break
    ans3 = ans3 + 1
    prev = r[i]
ans4 = 1
prev = r[-1]
for i in range(l - 2, 0, -1):
    if (r[i] == prev):
        break
    ans4 = ans4 + 1
    prev = r[i]
ans5 = ans3 + ans4
if (r[0] == r[-1]):
    print(ans1)
else:
    print(min(l, max(ans1, ans5)))
