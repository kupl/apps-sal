N = int(input())
for i in range(int(N / 4)+1):
    for j in range(int(N / 7)+1):
        total = 4*i + 7*j
        if total == N:
            print('Yes')
            return
else:
    print('No')

