N = int(input())

Flag = False

for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        if a * b == N:
            Flag = True

if Flag:
    print('Yes')
else:
    print('No')
