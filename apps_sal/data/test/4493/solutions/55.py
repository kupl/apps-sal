(c_1_1, c_1_2, c_1_3) = map(int, input().split())
(c_2_1, c_2_2, c_2_3) = map(int, input().split())
(c_3_1, c_3_2, c_3_3) = map(int, input().split())
ans = 'No'
for a_1 in range(101):
    b_1 = c_1_1 - a_1
    b_2 = c_1_2 - a_1
    b_3 = c_1_3 - a_1
    for a_2 in range(101):
        if c_2_1 != a_2 + b_1:
            continue
        if c_2_2 != a_2 + b_2:
            continue
        if c_2_3 != a_2 + b_3:
            continue
        for a_3 in range(101):
            if c_3_1 != a_3 + b_1:
                continue
            if c_3_2 != a_3 + b_2:
                continue
            if c_3_3 != a_3 + b_3:
                continue
            ans = 'Yes'
            break
        if ans == 'Yes':
            break
    if ans == 'Yes':
        break
print(ans)
