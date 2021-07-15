def calc_shortest(D, s1, s2):
    #D[1:3] = D[1]+D[2] = d_2+d_3 = distance between Station 2 and Station 4
    if s1 == s2:
        return 0
    elif s1 < s2:
        path1 = sum(D[s1-1:s2-1])
    else:
        path1 = sum(D[s2-1:s1-1])

    path2 = sum(D)-path1

    if path1 < path2:
        return path1
    else:
        return path2

N = [int(i) for i in input().strip().split()][0]
D = [int(i) for i in input().strip().split()]
s1, s2 = [int(i) for i in input().strip().split()]
print(calc_shortest(D, s1, s2))
return
