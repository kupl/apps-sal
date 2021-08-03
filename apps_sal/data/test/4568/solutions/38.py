N = int(input())
S = input()

res = 0
for i in range(1, N):
    com = set(S[:i]) & set(S[i:])
    if res < len(com):
        res = len(com)
print(res)
