n = int(input())
s = input()
len_t = n // 2
t = s[0:len_t] * 2
if t == s:
    print('Yes')
else:
    print('No')
