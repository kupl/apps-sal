(t1, t2, t3) = input().split()
ans = 2
if t1 == t2 or t2 == t3 or t3 == t1:
    if t1 == t2 == t3:
        ans = 0
    else:
        ans = 1
aaa = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            if k - j == j - i == 1:
                aaa.append({i, j, k})
if t1[1] == t2[1] == t3[1] and {int(t1[0]), int(t2[0]), int(t3[0])} in aaa:
    ans = 0
elif t1[1] == t2[1] and (abs(int(t1[0]) - int(t2[0])) == 1 or abs(int(t1[0]) - int(t2[0])) == 2) or (t1[1] == t3[1] and (abs(int(t1[0]) - int(t3[0])) == 1 or abs(int(t1[0]) - int(t3[0])) == 2)) or (t3[1] == t2[1] and (abs(int(t3[0]) - int(t2[0])) == 1 or abs(int(t3[0]) - int(t2[0])) == 2)):
    ans = min(1, ans)
print(ans)
