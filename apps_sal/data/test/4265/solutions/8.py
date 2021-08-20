S = str(input())
T = str(input())
result = 0
for i in range(len(T)):
    if S[i] != T[i]:
        result += 1
print(result)
