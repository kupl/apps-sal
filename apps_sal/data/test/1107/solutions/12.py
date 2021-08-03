n = input('')
n = int(n)
str = input('')
l = len(str)
count = 0
if l <= 4:
    print(0)
elif l > 4:
    c = n
    while c <= (l - 1):
        str1 = str[c - 3:c]
        if str1 == 'aaa' or str1 == 'bbb':
            count += 1
        c += n
    print(count)
