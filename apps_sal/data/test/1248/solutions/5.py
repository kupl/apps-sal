d1, d2, d3 = [int(i) for i in input().split()]
print(min(2 * (d1 + d2), d1 + d2 + d3, 2 * (d1 + d3), 2 *(d2 + d3)))

