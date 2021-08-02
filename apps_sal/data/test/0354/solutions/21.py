s = input()
t = input()

if len(s) != len(t):
    print("No")
else:
    v = "aeiou"
    c = "qwrtypsdfghjklzxcvbnm"
    flag = 0
    for i, j in zip(s, t):
        if (i in v and j not in v) or (i in c and j not in c):
            flag = 1
            break
    if flag:
        print("No")
    else:
        print("Yes")
