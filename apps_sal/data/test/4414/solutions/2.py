read = lambda: [int(i) for i in input().split()]

q = int(input())

for _ in range(q):
    a, b, n, S = read()
    spend_a = min(a, S // n)
    if S - spend_a * n > b:
        print('NO')
    else:
        print('YES')
