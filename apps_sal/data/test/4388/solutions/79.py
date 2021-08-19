n = list(input())
for i in range(3):
    if n[i] == '1':
        n[i] = '9'
    else:
        n[i] = '1'
S = ''
for j in range(3):
    S += n[j]
print(S)
