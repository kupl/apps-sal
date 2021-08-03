n = int(input())
for i in range(n):
    s = input()
    t = input()
    p = input()
    mas1 = [0] * 26
    flag = True
    for i in range(len(s)):
        mas1[ord(s[i]) - 97] += 1
    mas2 = [0] * 26
    x1 = 0
    for i in range(len(t)):
        if x1 < len(s) and s[x1] == t[i]:
            x1 += 1
        mas2[ord(t[i]) - 97] += 1
    if x1 != len(s):
        print("NO")
    else:
        mas3 = [0] * 26
        for i in range(len(p)):
            mas3[ord(p[i]) - 97] += 1
        for i in range(26):
            if mas3[i] + mas1[i] < mas2[i]:
                flag = False
        if flag == True:
            print("YES")
        else:
            print("NO")
