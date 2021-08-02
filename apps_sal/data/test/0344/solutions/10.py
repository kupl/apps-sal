s = input()
st = {'a', 'e', 'i', 'o', 'u'}
flag = "YES"
if(s[-1] != 'n' and not s[-1] in st):
    flag = "NO"
else:
    for i in range(0, len(s) - 1):
        if(s[i] == 'n'):
            continue
        if(s[i] in st):
            continue
        if(not s[i + 1] in st):
            flag = "NO"
            break
print(flag)
