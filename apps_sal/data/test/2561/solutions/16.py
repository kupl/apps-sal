t = int(input())
for i in range(t):
    ans = 1
    a = bin(int(input()))[2:]
    for j in a:
        if j == '1':
            ans *= 2
    print(ans)
