n, a, b = list(map(int, input().split()))
s = input()
ans = 0

A, B = a, b
cnt = 0
for i in s:
    if(i == '*'):
        if(cnt % 2):
            if(a > b):
                a -= cnt // 2 + 1
                b -= cnt // 2
            else:
                a -= cnt // 2
                b -= cnt // 2 + 1
        else:
            a -= cnt // 2
            b -= cnt // 2
        cnt = 0
    else:
        cnt += 1
if(cnt % 2):
    if(a > b):
        a -= cnt // 2 + 1
        b -= cnt // 2
    else:
        a -= cnt // 2
        b -= cnt // 2 + 1
else:
    a -= cnt // 2
    b -= cnt // 2
cnt = 0

if(a <= 0):
    if(b <= 0):
        print(A + B)
    else:
        print(A + B - b)
else:
    if(b <= 0):
        print(A - a + B)
    else:
        print(A - a + B - b)
