N = int(input())
S = input()
T = [0] * N
L = 0
for (i, s) in enumerate(S):
    if s == '(':
        L += 1
        T[i] = L
    else:
        T[i] = L
        L -= 1
print(''.join(['0' if t % 2 else '1' for t in T]))
