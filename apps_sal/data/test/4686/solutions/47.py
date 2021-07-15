W = input()
s = list(set(W))
l = len(s)


for i in range(l):
    for a in s[i]:
        if W.count(a)%2 == 1:
            print("No")
            return
        else:
            break
print("Yes")

