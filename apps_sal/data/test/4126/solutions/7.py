s = input()

if s == s[::-1]:
    f = s[:len(s)//2]
    b = s[len(s)//2 + 1:]
    if f == f[::-1] and b == b[::-1]:
        print('Yes')
        return

print('No')
