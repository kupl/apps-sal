n, m = list(map(int, input().split()))
if n > m:
    m, n = n, m
if n == 1:
    if m % 6 == 0:
        print(m)
    elif m % 6 <= 3:
        print(m - (m % 6))
    else:
        print(m - (6 - m % 6))
elif(n == 2 and m == 2):
    print(0)
elif(n == 2 and m == 3):
    print((4));
elif(n == 2 and m == 7):
    print(12)
else:
    if n % 2 and m % 2:
        print((n * m - 1));
    else:
        print(n * m)
# find the formula myself!
