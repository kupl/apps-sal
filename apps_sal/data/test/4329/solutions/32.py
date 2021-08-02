s = input()
t = input()
i = 0
bool = False
while i <= len(s) - 1:
    if s[i] != t[i]:
        print("No")
        bool = True
        break
    else:
        i = i + 1
if bool == False:
    print("Yes")
