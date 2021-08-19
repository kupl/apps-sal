S = list(input())
P = X = 753
for num in range(len(S) - 2):
    a = int(S[num] + S[num + 1] + S[num + 2])
    a = abs(P - a)
    if a <= X:
        X = a
print(X)
