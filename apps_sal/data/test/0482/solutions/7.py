(n, k) = map(int, input().split())
abc = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n):
    print(abc[i % k], end='')
print()
