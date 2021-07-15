def ans():
    n = int(input())
    c = bin(n).count("1")
    ans = pow(2, c)

    print(ans)

tc = int(input())
for _ in range(tc):
    ans()
