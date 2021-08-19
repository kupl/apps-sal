(a, b) = [int(i) for i in input().split()]
b_no_snow = sum(range(1, b - a + 1))
print(b_no_snow - b)
