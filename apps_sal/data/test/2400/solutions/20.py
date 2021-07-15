t = int(input())
for i in range(t):
    n = int(input())
    narr = list(map(int, input().split()))
    m = int(input())
    marr = list(map(int, input().split()))
    n0 = sum([1 for p in narr if p % 2 == 0])
    n1 = len(narr) - n0
    m0 = sum([1 for p in marr if p % 2 == 0])
    m1 = len(marr) - m0
    print(n0 * m0 + n1 * m1)
