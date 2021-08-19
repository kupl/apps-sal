S = input()
list = []
t = 0
while t <= 2:
    list.append(S[t])
    t = t + 1
if len(set(list)) == 1:
    print('No')
else:
    print('Yes')
