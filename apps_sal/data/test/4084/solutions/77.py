n,blue,red = list(map(int,input().split()))

# n / (blue + red) = quot ...rem
quot = n // (blue + red) #商 quotient
rem = n % (blue + red) #余り remainder

ans = blue * quot + min(blue,rem)

print(ans)
