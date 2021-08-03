n = int(input())
strs = input()
counta = []
countb = []
no1 = 0
no0 = 0
i = 0
while(i < len(strs)):
    if(strs[i] == '1'):
        no1 += 1
    else:
        no0 += 1
    counta.append(no1)
    countb.append(no0)
    i += 1
hashd = dict()
hashd[0] = [-1]
i = 0
maxm = 0
while(i < len(strs)):
    if((counta[i] - countb[i]) in hashd):
        hashd[(counta[i] - countb[i])].append(i)
        if(i - hashd[(counta[i] - countb[i])][0] > maxm):
            maxm = i - hashd[(counta[i] - countb[i])][0]
    else:
        hashd[counta[i] - countb[i]] = [i]
    i += 1
print(maxm)
