Ss = input().rstrip()

N = len(Ss)
S1s = Ss[:N // 2]
S2s = Ss[(N + 1) // 2:]
# print('# S1s:', S1s)
# print('# S2s:', S2s)

if Ss == Ss[::-1] and S1s == S1s[::-1] and S2s == S2s[::-1]:
    print('Yes')
else:
    print('No')
