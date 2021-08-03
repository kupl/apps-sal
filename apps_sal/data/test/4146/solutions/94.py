import collections

n = int(input())
v = [int(i) for i in input().split()]
con_odd = []
con_even = []
for i in range(0, n, 2):
    con_odd.append(v[i])
    con_even.append(v[i + 1])

b = collections.Counter(con_odd)
c = sorted(b.items(), key=lambda x: x[1], reverse=True)
b_2 = collections.Counter(con_even)
c_2 = sorted(b_2.items(), key=lambda x: x[1], reverse=True)
if len(c) == 1 and len(c_2) == 1:
    if c[0][0] == c_2[0][0]:
        ans = n // 2
    else:
        ans = 0
elif len(c) == 1 or len(c_2) == 1:
    if c[0][0] == c_2[0][0]:
        if len(c) == 1:
            ans_1 = len(con_odd) - c[0][1]
            ans_2 = len(con_even) - c_2[1][1]
            ans = ans_1 + ans_2
        else:
            ans_1 = len(con_odd) - c[1][1]
            ans_2 = len(con_even) - c_2[0][1]
            ans = ans_1 + ans_2
    else:
        ans_1 = len(con_odd) - c[0][1]
        ans_2 = len(con_even) - c_2[0][1]
        ans = ans_1 + ans_2

elif c[0][0] == c_2[0][0]:
    if c[0][1] + c_2[1][1] > c[1][1] + c_2[0][1]:
        ans_1 = len(con_odd) - c[0][1]
        ans_2 = len(con_even) - c_2[1][1]
        ans = ans_1 + ans_2
    else:
        ans_1 = len(con_odd) - c[1][1]
        ans_2 = len(con_even) - c_2[0][1]
        ans = ans_1 + ans_2
else:
    ans_1 = len(con_odd) - c[0][1]
    ans_2 = len(con_even) - c_2[0][1]
    ans = ans_1 + ans_2
print(ans)
