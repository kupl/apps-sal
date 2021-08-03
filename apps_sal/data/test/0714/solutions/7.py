
n = int(input())
a = sorted(enumerate(map(int, input().split())), key=lambda x: x[1])

for idx in range(n // 2):
    print('{} {}'.format(a[idx][0] + 1, a[-(idx + 1)][0] + 1))
