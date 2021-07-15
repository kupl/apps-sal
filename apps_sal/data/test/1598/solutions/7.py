S = list(map(int,input().strip()))
N = len(S)

stack = []
for i in range(N):
    s = S[i]
    if s == 0 and stack and stack[-1][0] == 1:
        stack.pop()
    else:
        stack.append((s, i))
T = S[:]
for i in tuple(map(list, list(zip(*stack))))[1]:
    T[i] = 0

print(''.join(map(str, T)))

