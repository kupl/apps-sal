t = int(input())
for i in range(t):
    ans = 0
    t1 = int(input())
    n = len(str(t1))
    ans = 9 * (n - 1)
    l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for el in l:
        if int(el * (n)) <= t1:
            ans += 1
        else:
            break
    print(ans)
