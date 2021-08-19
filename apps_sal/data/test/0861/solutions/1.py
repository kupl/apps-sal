m, R = [int(x) for x in input().split()]

if m == 1:
    print(2 * R)
else:
    tot = 0
    for i in range(m):
        tot += 2
        if i == 0 or i == m - 1:
            tot += 2 + 2**.5
            tot += (m - 2) * (m - 1)
            tot += 2 * 2**.5 * (m - 2)
        else:
            tot += 4 + 2 * 2**.5
            tot += i * (i - 1)
            tot += (m - i - 1) * (m - i - 2)
            tot += 2 * 2**.5 * (m - 3)
        # print(i,tot)
    tot *= R
    tot /= m * m
    print(tot)

# print(
# print(R*(2+(1+2**.5+(2*m-1)/3)*(m-1))/m)
# print(R*(1+m+m*2**.5-2**.5+(2*m*m/3)-m+1/3)/m)
# print(R*(1/m+2**.5-(2**.5)/m+2*m/3+1/3))
# print(R/m+R*2**.5-(R*2**.5)/m+2*R*m/3+R/3)
