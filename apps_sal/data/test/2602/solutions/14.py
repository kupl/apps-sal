tk = int(input())
for i in range(tk):
    (a, b, n, m) = map(int, input().split())
    if a + b < n + m:
        print('No')
        continue
    elif min(a, b) < m:
        print('No')
    else:
        print('Yes')
