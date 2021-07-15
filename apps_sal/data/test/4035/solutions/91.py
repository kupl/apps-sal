def main():
    a,b = map(int, input().split())
    ans = -1
    import math
    i = 1
    f= False
    while True:
        if math.floor( i * 0.08) == a and math.floor(i * 0.1) == b:
            ans = i
            f = True
            break
        elif math.floor( i * 0.08)>a or math.floor(i * 0.1) > b:
            f= False
            break
        i +=1
    return ans 
    
def __starting_point():
    print(main())
__starting_point()
