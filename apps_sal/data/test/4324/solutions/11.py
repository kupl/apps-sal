for i in range(int(input())):
    n, a, b = list(map(int, input().split()))
    k = 0
    f = ''
    for j in range(n):
        f += chr(k + ord('a'))
        k = k + 1
        k = k % b
    print(f)
