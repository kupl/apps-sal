for _ in range(int(input())):
    n, a, b = list(map(int, input().split()))
    s = input() + '0'
    min1, min2 = b, float('inf')
    for q in range(n):
        min3 = min(min1 + 2 * a + b * 2, min2 + a + b * 2)
        if s[q + 1] == '0' and s[q] == '0':
            min1 = min(min1 + a + b, min2 + 2 * a + b)
        else:
            min1 = float('inf')
        min2 = min3
    print(min1)
