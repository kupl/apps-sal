N = int(input())
(count, result) = (0, 0)
for i in range(N):
    (D1, D2) = map(int, input().split())
    if D1 == D2:
        count += 1
    else:
        count = 0
    if count == 3:
        result = 1
print('Yes' if result == 1 else 'No')
