s = input()
n = len(s)
k = True
for item in s:
    if(item in "02356789"):
        print("NO")
        k = False
        break
if(k):
    s = s.replace("144", "0")
    s = s.replace("14", "0")
    s = s.replace("1", "0")
    if(s.count("0") == len(s)):
        print("YES")
    else:
        print("NO")
