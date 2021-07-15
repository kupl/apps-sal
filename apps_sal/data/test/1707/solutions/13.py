import bisect

def main():
    n = int(input())
    pts = list(map(int,input().split()))
    points = []
    for i in range(n):
        points.append(abs(pts[i]))

    points.sort()
    #print(points)
    pairs = 0

    for i in range(n):
        x = points[i]
        index = bisect.bisect(points,2*x)-1
        #print(x,index)
        if points[index] <= 2*x:
            if index >= i:
                pairs += index-i

    print(pairs)
        


main()

