def main():
    n = int(input())
    k = 0
    i = 1
    while n // 10:
    
        k += 1*i if n % 10 == 4 else 2*i
        
        n //= 10
        i *= 2
    k += 1*i if n % 10 == 4 else 2*i
    print(k)
def __starting_point():
    main()

__starting_point()
