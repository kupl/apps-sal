N = int(input())
S = str(input())

M = 0
Sum = 0

for x in S:
    if x == 'I':
        Sum += 1
    else:
        Sum -= 1
    M = max(M, Sum)

print(M)
