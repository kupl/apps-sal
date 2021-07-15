
s_o = str(input().strip())
t_o = str(input().strip())
dic = []

for i in range(len(s_o)-len(t_o)+1):
    s = s_o
    t = t_o
    flg = 0
    for j in range(len(t_o)):
        if s[i+j] == t[j] or s[i+j] == "?":
            s = s[:i+j] + t[j] + s[i+j+1:]
        else:
            flg = 1
            break
    if flg:
        continue
    s = s.replace("?", "a")
    dic.append(s)

if len(dic) == 0:
    print("UNRESTORABLE")
else:
    dic.sort()
    print(dic[0])
