str10, str01 = '', ''
for i in range(5 * (10**4) + 1):
    str10 += '10'
    str01 += '01'

s = str(input())
len_s = len(s)
str10 = str10[:len_s]
str01 = str01[:len_s]
# print(str10,str01)

cnt10, cnt01 = 0, 0
for i in range(len_s):
    if s[i] != str10[i]:
        cnt10 += 1
    if s[i] != str01[i]:
        cnt01 += 1
print(min(cnt10, cnt01))
