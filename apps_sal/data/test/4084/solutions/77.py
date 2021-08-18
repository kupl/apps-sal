n, blue, red = list(map(int, input().split()))

quot = n // (blue + red)
rem = n % (blue + red)

ans = blue * quot + min(blue, rem)

print(ans)
