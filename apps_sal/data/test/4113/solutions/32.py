N = int(input())
for i in range(14):
    for j in range(25):
        if 7*i + 4*j == N:
            print('Yes')
            return

print('No')
