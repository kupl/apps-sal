def main():
    n = int(input())
    al = []
    bl = []
    for _ in range(n):
        a, b = map(int, input().split())
        al.append(a)
        bl.append(b)
    al.sort()
    bl.sort()
    if n%2:
        print(bl[n//2]-al[n//2]+1)
    else:
        print(bl[n//2]+bl[n//2-1]-al[n//2]-al[n//2-1]+1)
 
def __starting_point():
    main()
__starting_point()
