def main():
    linea = [int(x) for x in input().strip().split()]
    n = linea[0]
    m = linea[1]
    suma = 0
    linea = [int(x) for x in input().strip().split()]
    resp = 1
    for i in range(n):
        if(suma+linea[i] <=m):
            suma+=linea[i]
        else:
            resp+=1
            suma = linea[i]
    print(resp)
main()
