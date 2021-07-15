def change(x) :
    if x == x.upper() :
        return x.lower()
    if x == x.lower() :
        return x.upper()

s,t = input(), input()
L = [0]*256
for i in t :
    L[ord(i)] += 1

ans1 = ans2 = 0
P = []
for i in s :
    x = ord(i)
    if L[x] > 0 :
        L[x] -= 1
        ans1 += 1
    else :
        P.append(i)

for i in P :
    x = ord(change(i))
    if L[x] > 0 :
        L[x] -= 1
        ans2 += 1
print(ans1, ans2)

