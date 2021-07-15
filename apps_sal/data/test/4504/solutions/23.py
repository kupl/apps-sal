s = input()
for i in range(1,201):
    if (len(s)-i)%2 == 0:
        if s[:(len(s)-i)//2]*2 == s[:len(s)-i]:
            print(len(s[:len(s)-i]))
            break
