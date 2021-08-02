S = input()
zero = 0
one = 0
for i in range(len(S)):
    if S[i] == '1':
        one += 1
    else:
        zero += 1
print((min(zero, one) * 2))
