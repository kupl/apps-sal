def change(s):
    res = ""
    for i in range(len(s)):
        if s[i] == 'O' or s[i] == 'o':
            res += '0'
            continue
        if s[i] == 'l' or s[i] == 'L' or s[i] == 'i' or s[i] == 'I':
            res += '1'
            continue
        if s[i].isalpha() and s[i].isupper():
            res += s[i].lower()
            continue
        res += s[i]
    return res


a = change(input())
n = int(input())
for i in range(n):
    b = change(input())
    if a == b:
        print("No")
        return
print("Yes")

