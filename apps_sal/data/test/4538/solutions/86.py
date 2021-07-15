def main():
    
    n, d = map(int, input().split())
    cnt = 0
    # xy = [<>,<>,<>... ] <>はmapobj
    xy = [map(int, input().split()) for i in range(n)]
    # zip(*xy) = (x1, x2, s3, s4...), (y1, y2, y3, y4...)
    x, y = [list(i) for i in zip(*xy)]
        
    for i in range(n):
        if x[i]**2 + y[i]**2 <= d**2:
            cnt += 1
    print(cnt)
    
    
    
    
def __starting_point():
    main()
__starting_point()
