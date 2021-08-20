S = input()
T = input()
data = []
for i in range(len(S) - len(T) + 1):
    count = 0
    for j in range(len(T)):
        if S[i + j] != T[j]:
            count += 1
    data.append(count)
print(min(data))
