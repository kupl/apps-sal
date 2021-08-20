N = int(input())
S = input()
front = S[:N // 2]
latter = S[N // 2:]
if front == latter:
    print('Yes')
else:
    print('No')
