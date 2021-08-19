(N, D) = map(int, input().split())
kanshi = 2 * D + 1
print(N // kanshi if N % kanshi == 0 else N // kanshi + 1)
