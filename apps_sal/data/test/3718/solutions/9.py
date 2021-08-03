n = int(input())
a = list(map(int, input().split()))
b = set(a)
c = sorted(b)
for i in range(len(c) - 2):
    if c[i] - c[i + 2] >= -2:
        print('YES')
        break
else:
    print('NO')
