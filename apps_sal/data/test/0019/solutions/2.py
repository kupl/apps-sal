for tc in range(int(input())):
    n = int(input())
    (am, bm) = (0, 0)
    res = 'YES'
    for i in range(n):
        (a, b) = list(map(int, input().split()))
        if a < am or b < bm or a - b < am - bm:
            res = 'NO'
        (am, bm) = (a, b)
    print(res)
