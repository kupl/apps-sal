N = int(input())
S = input()
T = ''
for i in range(N):
    T = T + S[i]
    if len(T) > 2:
        if T[-3] == 'f' and T[-2] == 'o' and (T[-1] == 'x'):
            T = T[:-3]
print(len(T))
