n, c = map(int, input().split())

S = list(map(int, input().split()))
E = list(map(int, input().split()))

lastS = S[0]
lastE = E[0] + c
print('0 ',end='')
print(min(lastS, lastE), end= ' ')

for i in range(1, n - 1):
    curS = min(lastS + S[i], lastE + S[i])
    curE = min(lastS + c + E[i], lastE + E[i])
    print(min(curS, curE), end=' ')
    lastS = curS
    lastE = curE
