S = input()
T = input()

max_match = 0
temp_match = 0

for i in range(len(S) - len(T) + 1):
    for j in range(len(T)):
        if S[i + j] == T[j]:
            temp_match += 1
    if temp_match > max_match:
        max_match = temp_match
    temp_match = 0

print(len(T) - max_match)
