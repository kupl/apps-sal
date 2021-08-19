n = int(input())
s = input()

t = ""
for i in range(n):
    t += s[i]
    #print("t1 = " + t)
    while len(t) >= 3 and t[-3:] == "fox":
        t = t[:-3]
        #print("t2 = " + t)
print((len(t)))
