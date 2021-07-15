import  math

N = int(input())

p = (-1 + math.sqrt(1 + 8 * N)) // 2
N -= p * (p + 1) // 2

if N == 0:
    print(int(p))
else:
    print(int(N))

