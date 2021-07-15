S = input()
T = input()
ans = len(T)

for i in range(len(S)-len(T) + 1):
    ans = min(ans, sum([x[0] != x[1] for x in zip(T,S[i:]) ]))

print(ans)

