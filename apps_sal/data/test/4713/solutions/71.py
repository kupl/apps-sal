N = int(input())
S = input()
x = 0
X = [0]*(N+1)

for i in range(1, N+1):
    if S[i-1] == "I":
        x += 1
        X[i] = x
    else:
        x -= 1
        X[i] = x
print((max(X)))

