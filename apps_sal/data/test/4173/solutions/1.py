q = int(input())
for l in range(q):
    n, a, b = list(map(int, input().split()))
    if(2 * a <= b):
        print(n * a)
    else:
        print((n // 2) * b + (n % 2) * a)
