a = int(input())
t = ""
tt = ""
ttt = ""
if a % 2 != 0:
    for x in range(0, a):
        t = t + (str(x) + " ")
    for x in range(0, a):
        tt = tt + (str(x) + " ")
    for x in range(0, a):
        ttt = ttt + (str(2 * x % a) + " ")
else:
    print(-1)


print(t)
print(tt)
print(ttt)
