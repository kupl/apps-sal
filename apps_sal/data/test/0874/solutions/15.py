n = int(input())
if n % 2:
    print('-1')
else:
    print(' '.join(str(x + 2 - x % 2 * 2) for x in range(n)))
