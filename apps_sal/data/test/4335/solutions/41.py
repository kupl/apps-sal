N = int(input())
S = str(input())
tmp = str()
for i in range(N // 2):
    tmp += S[i]
if tmp * 2 == S:
    print('Yes')
else:
    print('No')
