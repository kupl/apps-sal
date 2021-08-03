n = int(input())
same = [False] * n
for i in range(n):
    d1, d2 = list(map(int, input().split()))
    if d1 == d2:
        same[i] = True
for i in range(n - 2):
    if same[i] and same[i + 1] and same[i + 2]:
        print('Yes')
        return
print('No')
