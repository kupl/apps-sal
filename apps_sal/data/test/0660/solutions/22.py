import math
(n, b, p) = list(map(int, input().split()))
m = n
bottles = 0
papers = p * n
while m > 1:
    k = 2 ** math.floor(math.log(m, 2))
    bottles += k * b
    bottles += k // 2
    m = m - k + k // 2
print(bottles, papers)
