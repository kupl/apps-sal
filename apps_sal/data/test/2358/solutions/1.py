a = input()
(ans, ans1) = ([], [])
(q1, q2) = (0, len(a) - 1)
while True:
    while q1 < len(a) and a[q1] == ')':
        q1 += 1
    while q2 > -1 and a[q2] == '(':
        q2 -= 1
    if q1 < q2:
        ans.append(q1 + 1)
        ans1.append(q2 + 1)
    else:
        break
    q1 += 1
    q2 -= 1
if len(ans) + len(ans1) == 0:
    print(0)
else:
    print(1)
    print(len(ans) + len(ans1))
    print(*ans, *ans1[::-1])
