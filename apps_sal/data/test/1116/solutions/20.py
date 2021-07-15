t = int(input())

for i in range (t):
    r, b, k = list(map(int,input().split()))
    if r > b:
        temp = r
        r = b
        b = temp
    a = b//r
    c = b % r
    if c == 0:
        a -= 1
    if c > 0 and r % c > 0:
        a += 1
    if a >= k:
        print("REBEL")
    else:
        print("OBEY")
