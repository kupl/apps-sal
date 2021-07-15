N,M = map(int, input().split())

a = 1
b = N
for i in range(M, 0, -1):
    if i%2 == M%2:
        print(a, a+i)
        a += 1
    else:
        print(b, b-i)
        b -= 1
