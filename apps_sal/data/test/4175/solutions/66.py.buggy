n = int(input())
S = input()
last = S[-1]
D = set()
D.add(S)
for i in range(n - 1):
    S = input()
    D.add(S)
    if S[0] == last:
        last = S[-1]
    else:
        print('No')
        return
if len(D) == n:
    print('Yes')
else:
    print('No')
