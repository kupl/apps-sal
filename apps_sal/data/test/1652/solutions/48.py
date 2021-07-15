def conform(string, i, Tmember):
    for t in Tmember:
        if s[i] != t:
            print("NO")
            return
        else:
            i += 1
    return i


S = str(input())
T = ["maerd", "remaerd", "esare", "resare"]
s = ""
for i in range(1, len(S)+1):
    s += S[-i]
count = 0
while(count < len(s)):
    flag = 4
    if s[count] == "m":
        flag = 0
    elif (s[count] == "r")and(s[count+1] == "e")and(s[count+2] == "m"):
        flag = 1
    elif s[count] == "e":
        flag = 2
    elif (s[count] == "r")and(s[count+1] == "e")and(s[count+2] == "s"):
        flag = 3
    else:
        print("NO")
        return
    count = conform(s, count, T[flag])
print("YES")

