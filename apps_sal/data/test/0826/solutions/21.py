import math
N = int(input())
OK = 0
NG = 10 ** 10
while NG - OK > 1:
    check = (OK + NG) // 2
    if check * (check + 1) <= 2 * N + 2:
        OK = check
    else:
        NG = check
print(N - OK + 1)
