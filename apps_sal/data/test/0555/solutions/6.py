S = list(input())
for i in range(len(S)):
    x = int(S[i])
    y = 9 - x
    if y < x and (y != 0 or i != 0):
        S[i] = str(y)
print(''.join(S))
