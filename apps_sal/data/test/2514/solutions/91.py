from collections import defaultdict
def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    q = int(input())
    bc = []
    sum1 = sum(a)
    for _ in range(q):
        bc.append(list(map(int, input().split(" "))))
    d = defaultdict(lambda:0)
    for i in range(n):
        d[a[i]] += 1

    for i in range(q):
        if bc[i][0] in d:
            sum1 += (bc[i][1] - bc[i][0]) * d[bc[i][0]]
            d[bc[i][1]] += d[bc[i][0]]
            del d[bc[i][0]] 
        print(sum1)
        

def __starting_point():
    main()
__starting_point()
