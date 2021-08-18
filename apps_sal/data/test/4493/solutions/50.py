c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))
c = [c1, c2, c3]
for a1 in range(100):
    b1 = c1[0] - a1
    b2 = c1[1] - a1
    b3 = c1[2] - a1
    a21 = c2[0] - b1
    a22 = c2[1] - b2
    a23 = c2[2] - b3
    a31 = c3[0] - b1
    a32 = c3[1] - b2
    a33 = c3[2] - b3
    if (a21 == a22 == a23) and (a31 == a32 == a33):
        print('Yes')
        break
    elif a1 == 99:
        print('No')
        break
    else:
        continue
