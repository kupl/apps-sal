a, b = list(map(int, input().split()))
if a == b:
    print(a)
else:
    a -= 1
    if a%2 == 0:
        fa = (a//2)%2 ^ a
    else:
        fa = ((a+1)//2)%2
    if b%2 == 0:
        fb = (b//2)%2 ^ b
    else:
        fb = ((b+1)//2)%2
    print((fb ^ fa))

