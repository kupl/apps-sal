n, a = int(input()), list(map(int, input().split()))
b = [a[1::2][::-1] + a[::2], a[0::2][::-1] + a[1::2]][n % 2]
print(*b, sep=' ')
