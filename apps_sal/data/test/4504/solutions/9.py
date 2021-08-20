S = list(input())
for _ in range(len(S) - 1):
    del S[-1]
    if S[:int(len(S) / 2)] == S[int(len(S) / 2):]:
        break
print(len(S))
