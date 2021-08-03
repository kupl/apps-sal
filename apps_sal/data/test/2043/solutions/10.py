s = input()
a = input()
j = 0
v = 0
c = 0
flag = 0
if len(s) > len(a):
    pass
else:
    for i in range(len(s)):
        k = s[i]
        while j < len(a):
            if a[j] == k:
                flag += 1
                if flag == len(s):
                    c = j
                    break
                else:
                    break
            j += 1
        j += 1
    j = len(a) - 1
    flag = 0
    for i in range(len(s) - 1, -1, -1):
        k = s[i]
        while j > c:
            if a[j] == k:
                flag += 1
                if flag == len(s):
                    v = j - c
                    break
                else:
                    break
            j -= 1
        j -= 1
print(v)
