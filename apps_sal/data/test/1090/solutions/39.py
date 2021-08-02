N, K = map(int, input().split())
S = input()
Hap = 0
NewS = S[0]


def chan(X):
    if X == 'R':
        return 'L'
    else:
        return 'R'


for i in range(1, len(S)):
    strS = S[i]
    strS1 = S[i - 1]
    if strS != strS1:
        NewS += strS
    else:
        Hap += 1
while len(NewS) > 1 and K != 0:
    Hap += 2
    NewS = chan(NewS[-1]) + NewS[2:-2] + chan(NewS[0])
    K -= 1
if Hap > N - 1:
    Hap = N - 1
print(Hap)
