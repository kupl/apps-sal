T = int(input())
for _ in range(T):
    x = input()
    y = input()
    x = x[::-1]
    y = y[::-1]
    p = -1
    for i in range(len(y)):
        if y[i] == '1':
            p = i 
            break
    q = -1
    for i in range(len(x)):
        if x[i] == '1' and i >= p:
            q = i
            break
    ans = q - p
    print(ans)

