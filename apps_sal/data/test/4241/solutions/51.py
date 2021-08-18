S = input()
T = input()

num = [0] * len(S)

for i in range(len(S) - len(T) + 1):
    for t in range(len(T)):
        if S[i + t] == T[t]:
            num[i] += 1

print(len(T) - max(num))
