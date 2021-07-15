n = int(input())
if n % 2 == 0:
    print(-1)
else:
    a = ' '.join(str(x) for x in range(n))
    print(a)
    print(a)
    print(' '.join(str(x) for x in range(0, n, 2)), 
          ' '.join(str(x) for x in range(1, n, 2)))
