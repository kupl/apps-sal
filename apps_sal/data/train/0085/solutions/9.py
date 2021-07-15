for _ in range(int(input())):
    s = input()
    n = len(s)
    x = int(input())
    
    w = ['1'] * len(s)
    
    for i in range(n):
        if s[i] == '0':
            if i + x < n:
                w[i + x] = '0'
            if i - x >= 0:
                w[i - x] = '0'
    
    temp = ['0'] * len(s)
    for i in range(n):
        if i + x < n:
            if w[i + x] == '1':
                temp[i] = '1'
        if i - x >= 0:
            if w[i - x] == '1':
                temp[i] = '1'
    if ''.join(temp) == s:
        print(''.join(w))
    else:
        print(-1)
