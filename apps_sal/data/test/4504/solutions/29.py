s = str(input())
for i in range(len(s)):
    s = s[:len(s)-1]
    if len(s)%2 == 0:
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        if a == b:
            print(len(s))
            break
