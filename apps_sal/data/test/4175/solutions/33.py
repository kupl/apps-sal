n = int(input())
tmp1=input()
tmp=tmp1[len(tmp1)-1]

s = set()
s.add(tmp1)

flg=True
for i in range(n-1):
    w = input()
    if w[0] != tmp:
        flg = False
        break
    tmp = w[len(w)-1]

    s.add(w)
    if(len(s) != i+2):
        flg = False
        break

if flg:
    print('Yes')
else:
    print('No')
