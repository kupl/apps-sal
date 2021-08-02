# ソートかけてどちらも同じだとYES

c1 = list(input())
c2 = list(input())

# print(c1)
# print(c2)

c1_str = ''.join(c1)
# c2_str = ''.join(c2)

c2_str_reverse = c2[2] + c2[1] + c2[0]

if c1_str == c2_str_reverse:
    print('YES')
else:
    print('NO')
