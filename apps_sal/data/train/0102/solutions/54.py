t = int(input())
for i in range(t):
    s = input()
    q = int(s[0])
    if int(s) >= int(str(q) * len(s)):
        print(q + (len(s) - 1) * 9)
    else:
        print(q - 1 + (len(s) - 1) * 9)
