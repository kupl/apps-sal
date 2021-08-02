suma, xor = list(map(int, input().split()))
mitad = round((suma - xor) / 2)
if(mitad < 0 or mitad * 2 + xor != suma or (mitad & xor) != 0):
    print(0)
else:
    print(2**(bin(xor).count("1")) - 2 * (suma == xor))
