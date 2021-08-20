from collections import defaultdict
n = int(input())
tc = 2 * n - 2
total = []
for _ in range(tc):
    string = input().strip()
    total.append((string, _))
total.sort(key=lambda x: x[0])
total.sort(key=lambda x: len(x[0]))
x1 = total[tc - 2][0]
x2 = total[tc - 1][0]
ans = x1 + x2[-1]
ans1 = x2 + x1[-1]
if x1[1:] == x2[:-1]:
    pass
else:
    (ans, ans1) = (ans1, ans)
alt = False
ans_dict = defaultdict()
for i in range(0, tc, 2):
    str1 = total[i][0]
    str2 = total[i + 1][0]
    idx1 = total[i][1]
    idx2 = total[i + 1][1]
    assert len(str1) == len(str2)
    if str1 == ans[:len(str1)] and str2 == ans[-len(str1):]:
        ans_dict[idx1] = 'P'
        ans_dict[idx2] = 'S'
    elif str2 == ans[:len(str1)] and str1 == ans[-len(str1):]:
        ans_dict[idx1] = 'S'
        ans_dict[idx2] = 'P'
    else:
        alt = True
if alt == True:
    ans = ans1
    for i in range(0, tc, 2):
        str1 = total[i][0]
        str2 = total[i + 1][0]
        idx1 = total[i][1]
        idx2 = total[i + 1][1]
        if str1 == ans[:len(str1)] and str2 == ans[-len(str1):]:
            ans_dict[idx1] = 'P'
            ans_dict[idx2] = 'S'
        elif str2 == ans[:len(str1)] and str1 == ans[-len(str1):]:
            ans_dict[idx1] = 'S'
            ans_dict[idx2] = 'P'
for i in range(0, tc):
    print(ans_dict[i], end='')
print()
