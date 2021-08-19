(l, r, a) = list(map(int, input().split()))
print(2 * max((min(l + i, r + a - i) for i in range(a + 1))))
