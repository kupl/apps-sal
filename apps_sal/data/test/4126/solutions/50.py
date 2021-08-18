S = input()
N = len(S)
Sf = S[0:(N - 1) // 2]
NSf = len(Sf)
Sb = S[(N + 3) // 2 - 1:N + 1]
NSb = len(Sb)
ans = 0

for i in range(N // 2):
    if S[i:i + 1] != S[N - 1 - i:N - i]:
        ans = 1

for i in range(NSf // 2):
    if Sf[i:i + 1] != Sf[NSf - 1 - i:NSf - i]:
        ans = 1

for i in range(NSb // 2):
    if Sb[i:i + 1] != Sb[NSb - 1 - i:NSb - i]:
        ans = 1

print('Yes') if ans == 0 else print('No')
