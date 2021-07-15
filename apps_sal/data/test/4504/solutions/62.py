s = input()
for i in range(len(s)):
    ss = s[:-2-i]
    size = len(ss)
    if size%2==0 and ss[:size//2] == ss[size//2:]:
        print(size)
        return
