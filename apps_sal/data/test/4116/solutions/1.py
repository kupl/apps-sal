N = int(input())

productos = []

def mult(N):
    for i in range(1,10):
        for n in range(1,10):

            calc = n * i
            productos.append(calc)

    if N in productos:
        print("Yes")
    else:
        print("No")
mult(N)
