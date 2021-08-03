n, k = map(int, input().split())
s = input()
if n == 1:
    if k >= 1:
        print(0)
        return
    else:
        print(s)
        return
else:
    s = list(s)
    if k > n:
        k = n
    ans = []
    for i in range(n):
        if k == 0:
            break
        if i == 0:
            if s[i] != '1':
                s[i] = '1'
                k -= 1
        else:
            if s[i] != '0':
                s[i] = '0'
                k -= 1
    print(''.join(s))
