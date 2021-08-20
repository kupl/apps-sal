t = int(input())
while t:
    n = int(input())
    ch = 0
    for i in range(100000):
        if i * (i - 1) // 2 > n:
            ch = i - 1
            break
    rem = n - ch * (ch - 1) // 2
    s = '1'
    s = s + '33' + '7' * rem + '3' * (ch - 2) + '7'
    print(s)
    t -= 1
