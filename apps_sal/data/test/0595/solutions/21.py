n = int(input())
st = n
vis = n % 400 == 0 or n % 4 == 0 and n % 100 != 0
now = 7
while now != 0 or vis != (n % 400 == 0 or n % 4 == 0 and n % 100 != 0):
    n += 1
    if n % 400 == 0 or n % 4 == 0 and n % 100 != 0:
        now += 2
        now %= 7
    else:
        now = (now + 1) % 7
print(n)

