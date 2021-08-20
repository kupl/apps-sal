n = int(input())
orgn = n
m = n - 1
orgm = m
ncounter = 1
mcounter = 1
for i in range(2, int(m ** 0.5) + 1):
    if m % i == 0:
        tmpc = 1
        m //= i
        while m % i == 0:
            tmpc += 1
            m //= i
        mcounter *= tmpc + 1
if m == orgm and m != 1:
    mcounter += 1
elif m > int(orgm ** 0.5):
    mcounter *= 2
mcounter -= 1
for i in range(2, int(n ** 0.5) + 1):
    if orgn % i == 0:
        n = orgn // i
        while n % i == 0:
            n //= i
        if n % i == 1:
            ncounter += 1
print(ncounter + mcounter)
