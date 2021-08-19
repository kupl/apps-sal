S = input()
b = []
for i in range(len(S) - 1):
    if S[i:i + 2] == '01' or S[i:i + 2] == '10':
        b.append(len(S) - (i + 1) if i < len(S) // 2 else i + 1)
print(min(b) if len(b) != 0 else len(S))
