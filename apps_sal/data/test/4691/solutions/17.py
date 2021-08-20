N = int(input())
S = ['' for i in range(N)]
for i in range(N):
    S[i] = str(input())
item = [0, 0, 0, 0]
rslt = ['AC', 'WA', 'TLE', 'RE']
for i in range(N):
    if S[i] == rslt[0]:
        item[0] += 1
    elif S[i] == rslt[1]:
        item[1] += 1
    elif S[i] == rslt[2]:
        item[2] += 1
    else:
        item[3] += 1
for i in range(4):
    print(rslt[i], 'x', item[i])
