s = input()
string1 = ""
string2 = ""
flag = 0
n = len(s)
for i in range(n):
    string1 += s[i]
    if(s[i] != "a"):
        string2 += s[i]
    if(string1 + string2) == s:
        flag = 1
        break
if(flag == 0):
    print(":(")
else:
    print(string1)
