D, N = map(int, input().split())
n = 1
while True:
    if n % (100**D) == 0 and n % (100**(D + 1)) != 0:
        N -= 1
    if N == 0:
        print(n)
        break
    n += 1
