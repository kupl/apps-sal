n = int(input())
i = 1
while i * i < n:
    l = ( n - i*i - i - 1 )
    if l > 0 and l % (2 * i) == 0:
        print(i, l // (2 * i) )
        break
    i += 1
else:
    print("NO")

