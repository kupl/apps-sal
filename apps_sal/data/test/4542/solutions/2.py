S = str(input())
Sum = 0
for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        Sum += 1

print(Sum)
