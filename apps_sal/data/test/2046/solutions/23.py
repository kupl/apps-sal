n = int(input())
maxsn = n-1
a = list(map(int, input().split()))
snacks = [0] * 100001
for i in range(n):
    snacks[a[i]-1] = 1
    while snacks[maxsn] == 1:
        snacks[maxsn] = 0
        print(maxsn + 1, end=' ')
        maxsn -= 1
    print()

