s = list(input())
s_front = s[:(len(s) // 2)]
s_back = s[::-1][:(len(s) // 2)]

result = 'Yes'

for f, f_r, b, b_r in zip(s_front, s_front[::-1], s_back, s_back[::-1]):
    if f != f_r or b != b_r or f != b:
        result = 'No'

print(result)
