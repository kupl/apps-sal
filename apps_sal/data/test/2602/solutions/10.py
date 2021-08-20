t = int(input())
for _ in range(t):
    (a, b, n, m) = map(int, input().split())
    if n + m > a + b:
        print('No')
        continue
    if min(a, b) < m:
        print('No')
        continue
    print('Yes')
