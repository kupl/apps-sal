def f(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1


s = int(input())
cnt = 0
a = [s]
while True:

    temp = f(a[cnt])

    if temp in a:
        print((len(a)+1))
        return
    a.append(temp)
    cnt += 1

