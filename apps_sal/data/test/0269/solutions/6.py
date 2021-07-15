s = input()
trr = [0 for i in range(4)]
prr = ['a', 'b', 'c', 'd']
for i in range(len(s)):
    if(s[i]!='!'):
        prr[i%4] = s[i]
    else:
        trr[i%4] += 1

krr = [0, 0, 0, 0]
for i in range(4):
    if(prr[i]=='R'):
        krr[0] = trr[i]
    if (prr[i] == 'B'):
        krr[1] = trr[i]
    if (prr[i] == 'Y'):
        krr[2] = trr[i]
    if (prr[i] == 'G'):
        krr[3] = trr[i]

print(krr[0], krr[1], krr[2], krr[3])
