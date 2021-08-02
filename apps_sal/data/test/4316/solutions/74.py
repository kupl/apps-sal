S = str(input())
hantei = 0

for i in range(len(S)):
    if S.count(S[i]) == 2:
        hantei += 1

if hantei == 4:
    print('Yes')
else:
    print('No')
