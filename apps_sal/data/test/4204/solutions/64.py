S = input()
K = int(input())
one = 0
for i in range(len(S)):
    if S[i] == '1':
        one += 1
    else:
        break
if K <= one:
    print('1')
else:
    print((S[one]))
