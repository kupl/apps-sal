def f():
    (a, b) = map(int, input().split())
    s = input()
    ToF = False
    c = 0
    ans = 0
    for item in s:
        if ToF:
            if item == '0':
                c += 1
            else:
                ans += min(c * b, a)
                c = 0
        if item == '1':
            ToF = True
    print(ans + a * ToF)


t = int(input())
for i in range(t):
    f()
