N = int(input())

ans = False
for i in range(N // 4 + 1):
    for j in range(N // 7 + 1):
        if 4 * i + 7 * j == N:
            ans = True
            break

if ans == True:
    print('Yes')
else:
    print('No')
