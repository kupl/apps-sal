N = int(input())
l = []
for i in range(1, 10):
    for h in range(1, 10):
        l.append(i * h)
print('Yes' if N in l else 'No')
