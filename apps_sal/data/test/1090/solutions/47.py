(N, K) = (int(i) for i in input().split())
S = input()
while 'LL' in S:
    S = S.replace('LL', 'L')
while 'RR' in S:
    S = S.replace('RR', 'R')
sad = N - len(S)
sad += K * 2
sad = min(N - 1, sad)
print(sad)
