n, a = int(input()), list(map(int, input().split()))
print(*[a[1::2][::-1] + a[::2], a[0::2][::-1] + a[1::2]][n % 2], sep=' ')
