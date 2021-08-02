S = input()
length = 0
for i in range(0, len(S) + 1):
    for j in range(i, len(S) + 1):
        T = S[i:j]
        if T.replace('A', '').replace('C', '').replace('G', '').replace('T', '') == '':
            if len(T) > length:
                length = len(T)
print(length)
