n = int(input())
s = input()
flag = True
while flag:
    s1 = ''
    n1 = len(s)
    m = 95
    ind = -1
    for i in range(len(s)):
        k = 0
        a = ord(s[i])
        if i < n1 - 1:
            if ord(s[i + 1]) - a == -1:
                if a > m:
                    m = a
                    ind = i
                continue
        if i > 0:
            if ord(s[i - 1]) - a == -1:
                if a > m:
                    m = a
                    ind = i
                continue
    if ind == -1:
        break
    s = s[0:ind] + s[ind + 1:n1]
print(n - len(s))
