s = input()
t = input()
total = False
for i in range(len(s)):
    s = s[len(s) - 1] + s[0:len(s) - 1]
    if s == t:
        print("Yes")
        total = True
        break
if total == False:
    print("No")
