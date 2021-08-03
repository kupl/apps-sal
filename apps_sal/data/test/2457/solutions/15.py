n_cases = int(input())
for case_num in range(n_cases):
    n, a, b, c, d = [int(x) for x in input().split()]
    lo = n * (a - b)
    hi = n * (a + b)
    if lo > c + d or hi < c - d:
        print("No")
    else:
        print("Yes")
