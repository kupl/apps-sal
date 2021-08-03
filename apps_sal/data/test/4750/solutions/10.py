t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    aa = [(a, b, 0), (c, d, 1)]
    aa.sort()
    one = aa[0][0]
    two = 0
    if(aa[1][0] != one):
        two = aa[1][0]
    else:
        two = aa[1][1]
    if(aa[0][2] == 0):
        print(one, two)
    else:
        print(two, one)
