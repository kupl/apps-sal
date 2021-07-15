s = input()
for i in range(1,len(s)):
    if s[:(len(s)-i)//2] == s[(len(s)-i)//2:-i]:
        print(len(s)-i)
        break
