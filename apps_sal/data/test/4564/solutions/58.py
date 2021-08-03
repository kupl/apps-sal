S = str(input())
data1 = []
for i in range(len(S)):
    data1.append(S[i])
data2 = list(set(data1))

if len(data1) == len(data2):
    print('yes')
else:
    print('no')
