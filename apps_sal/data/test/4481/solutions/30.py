N = int(input())
S = dict()
for i in range(N):
    s = input()
    if s in S:
        S[s] += 1
    else:
        S[s] = 1
max_val = max(S.values())
max_key = [key for key in S if S[key] == max_val]
print('\n'.join(sorted(max_key)))
