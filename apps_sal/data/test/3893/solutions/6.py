def main():
    rdl = list(map(int, input().split()))
    x1, y1 = rdl
    rdl = list(map(int, input().split()))
    x2, y2 = rdl
    n = int(input())
    Steps = 0
    for i in range(n):
        rdl = list(map(int, input().split()))
        if rdl[1] * y1 + rdl[0] * x1 + rdl[2] > 0 and rdl[1] * y2 + rdl[0] * x2 + rdl[2] < 0:
            Steps += 1
        elif rdl[1] * y1 + rdl[0] * x1 + rdl[2] < 0 and rdl[1] * y2 + rdl[0] * x2 + rdl[2] > 0:
            Steps += 1
    print(Steps)


main()
