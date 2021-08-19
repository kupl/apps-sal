for nt in range(int(input())):
    (a, b, n, m) = map(int, input().split())
    if n + m > a + b:
        print('No')
        continue
    if m > min(a, b):
        print('No')
        continue
    print('Yes')
