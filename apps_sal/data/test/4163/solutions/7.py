N = int(input())
count = 0
for _ in range(N):
    D1, D2 = map(int, input().split())
    if D1 == D2:
        count += 1
    else:
        count = 0

    if count == 3:
        print('Yes')
        return
print('No')
