result1 = 0
S = input()
l = len(S)
for i in range(l):
    if i % 2 == 0:
        if S[i] == '0':
            result1 += 1
    elif S[i] == '1':
        result1 += 1
print(min(result1, l - result1))
