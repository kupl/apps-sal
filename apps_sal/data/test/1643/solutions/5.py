s = input()[::-1]
count = 0
n = len(s)
s1 = ""
for i in range(n):
    if s[i] == '0':
        count += 1
        s1 += '0'
    elif count > 0:
        count -= 1
        s1 += '1'
    else:
        s1 += '0'
s1 = s1[::-1]
print(s1)
