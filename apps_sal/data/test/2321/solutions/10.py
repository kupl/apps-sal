for _ in range(int(input())):
    n = int(input())
    s = input()
    k = 0
    for i in range(n - 1, -1, -1):
        if s[i] is '<':
            k = n - 1 - i
            break

    for i in range(n):
        if s[i] is '>':
            k = min(k, i)
            break
    print(k)
