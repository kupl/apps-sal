for _ in range(int(input())):
    s = input() + '0'
    A = []
    tr = False
    x = 0
    for i in range(len(s)):
        if s[i] == '1':
            if tr:
                x += 1
            else:
                tr = True
                x = 1
        else:
            if tr:
                tr = False
                A.append(x)
    A.sort(reverse=True)
    Ans = 0
    for i in range(len(A)):
        if i % 2 == 0:
            Ans += A[i]
    print(Ans)
