a, b = map(int, input().split())

for c in range(1, 3):
    if a * b * c % 2 == 1:
        print('Yes')
        return
print('No')
