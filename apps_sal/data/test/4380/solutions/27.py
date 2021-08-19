(a, b) = map(int, input().split())
cnt = 0
for i in range(1, 4):
    if a * b * i % 2 == 1:
        cnt += 1
print('Yes' if cnt > 0 else 'No')
