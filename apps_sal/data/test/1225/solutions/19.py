h = int(input())

for i in range(10**12):
    if 2**i <= h < 2**(i + 1):
        ans = 2**(i + 1) - 1
        print(ans)
        return
