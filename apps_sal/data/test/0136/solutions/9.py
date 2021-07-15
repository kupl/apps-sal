a = str(input())
b = str(input())
len1 = len(a)
len2 = len(b)
first1 = -1
first2 = -1
for i in range(len1):
    if a[i] != '0'and first1 == -1:
        first1 = i
        break
for i in range(len2):
    if b[i] != '0' and first2 == -1:
        first2 = i
        break
flag = 0
if first1 == -1:
    first1 = len1 - 1
if first2 == -1:
    first2 = len2 - 1
if len1 - first1 > len2 - first2 :
    flag = 1
    print('>')
elif len1 - first1 < len2 - first2:
    flag = 1
    print('<')
else:
    for i in range(first1, len1):
        if a[i] > b[i-first1+first2]:
            flag = 1
            print('>')
            break
        elif a[i] < b[i-first1+first2]:
            flag = 1
            print('<')
            break
if flag == 0:
    print('=')
