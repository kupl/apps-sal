n,m = map(int, input().split())
cd = 0
while n > 0:
    cd += 1
    n -= 1
    if cd % m == 0:
        n += 1
print(cd)
