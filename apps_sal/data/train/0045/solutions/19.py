l = [1]
for i in range(70):
    l.append(2*l[-1] + 1)
# print(l[-1])
l = [(ll * (ll+1))//2 for ll in l]
lll = [l[0]]
for i in range(1, 70):
    lll.append(lll[-1] + l[i])
l = lll

for t in range(int(input())):
    n = int(input())
    for i in range(70):
        if l[i] > n:
            print(i)
            break
