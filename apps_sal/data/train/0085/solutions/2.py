t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    x = int(input())
    w = [0] * n
    for i in range(n):
        if 0 <= i + x < n and 0 <= i - x < n:
            if s[i + x] == '1' and s[i - x] == '1':
                w[i] = 1
        elif 0 <= i + x < n:
            if s[i + x] == '1':
                w[i] = 1
        elif 0 <= i - x < n:
            if s[i - x] == '1':
                w[i] = 1
    for i in range(n):
        if 0 <= i - x < n and w[i - x] == 1:
            if s[i] == '1':
                continue
            else:
                print(-1)
                break
        if 0 <= i + x < n and w[i + x] == 1:
            if s[i] == '1':
                continue
            else:
                print(-1)
                break
        if s[i] == '1':
            print(-1)
            break
    else:
        print(*w, sep='')
