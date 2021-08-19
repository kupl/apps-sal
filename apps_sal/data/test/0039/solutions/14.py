#l=[(int(i))for i in input().split()]
s = input()
if(s.count(s[0]) == len(s)):
    print(0)
elif s == s[::-1]:
    print(len(s) - 1)
else:
    print(len(s))
