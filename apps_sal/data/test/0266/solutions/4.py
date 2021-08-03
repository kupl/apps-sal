n, s = map(int, input().split())
if(n == 1 and s == 0):
    print('0 0')
elif(9 * n < s or s == 0):
    print('-1 -1')
else:
    res1 = 10**(n - 1)
    for i in range(s - 1):
        res1 += 10**(i // 9)
    res2 = 0
    for i in range(s):
        res2 += 10**(n - 1 - i // 9)
    print(res1, res2)
