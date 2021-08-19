t = int(input())
for i in range(t):
    n = int(input())
    e = (n + 3) // 4
    print('9' * (n - e) + '8' * e)
