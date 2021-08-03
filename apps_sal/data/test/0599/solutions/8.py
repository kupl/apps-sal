s = input()
lens = len(s)
flag = 0
for i in range(0, lens + 1):
    for j in range(ord('a'), ord('z') + 1):
        s1 = s
        s1 = s[:i] + chr(j) + s[i:]
        s2 = s1[::-1]
        if(s1 == s2):
            print(s1)
            flag = 1
            break
    if(flag == 1):
        break
if(flag == 0):
    print("NA")
