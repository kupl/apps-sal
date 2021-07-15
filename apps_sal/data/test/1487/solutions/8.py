s = input()
t = input()

n = len(s)
dist = 0

for i in range(n):
    if (s[i] !=t[i]):
        dist += 1

if dist%2==1:
    print("impossible")
else:
    p = ""
    flag = 0
    for i in range(n):
        if (s[i] != t[i] and flag == 0):
            p += s[i]
            flag = flag^1
        elif (s[i] != t[i] and flag == 1):
            p += t[i]
            flag = flag^1
        elif (s[i] == t[i]):
            p += s[i]
    print(p)

