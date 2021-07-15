N = int(input())

for x in range(1,10):
    for y in range(1,10):
        if x * y == N:
            print('Yes')
            return
print('No')
