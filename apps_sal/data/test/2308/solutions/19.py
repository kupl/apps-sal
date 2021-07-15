t = int(input())
for i in range(t):
    a = input()[::-1]
    b = input()[::-1]
    j = 0
    while b[j] == '0':
        j += 1
    res = 0
    while a[j] == '0':
        j += 1
        res += 1
    print(res)
