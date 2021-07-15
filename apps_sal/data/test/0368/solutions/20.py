# sorry for the source code iam a newbie in Python
chess = []
for i in range(8):
    chess.append(input())
s = 'qrbnpk'
w = [9,5,3,3,1,0]
D = dict(list(zip(s,w)))
D1 = dict(list(zip(s.upper(),w)))
dic = dict.fromkeys(s,0)
dic2 = dict.fromkeys(s.upper(),1)
dic2.update(dic)
res = [0,0]
for i in range(8):
    for j in range(8):
        if chess[i][j] != '.':
            res[dic2[chess[i][j]]] += D[chess[i][j].lower()]
first = res[0]
sec = res[1]
if first > sec:
    print ('Black')
elif first == sec:
    print ('Draw')
else:
    print ('White')

