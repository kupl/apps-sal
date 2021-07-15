def main():
    x = int(input())
    f = x//500
    rest = x-f*500
    s = rest//5
    total =  f*1000 +s*5
    return total
    

def __starting_point():
    print(main())
__starting_point()
