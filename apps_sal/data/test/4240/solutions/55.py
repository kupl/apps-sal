s = input()
t = input()


if t == s:
    print('Yes')
    return
else:
    for i in range(1,len(s)):
        st = s[-i:]+s[:len(s)-i]

        if st == t:
            print('Yes')
            return

print('No')
