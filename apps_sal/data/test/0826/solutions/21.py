import math
N = int(input())
# N+1 で、 1からkまで削り出せるとする
# k(k+1) = 2*N+2
OK = 0  # k(k+1)<=2N+2
NG = 10**10
while NG - OK > 1:
    check = (OK + NG) // 2
    if check * (check + 1) <= 2 * N + 2:
        OK = check
    else:
        NG = check
print(N - OK + 1)
