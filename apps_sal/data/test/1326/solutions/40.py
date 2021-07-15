import numba

@numba.njit
def main(N):
    x = 0
    for i in range(1,N+1):
        for j in range(i,N+1,i):
            x += j
    return x
N = int(input())
print(main(N))
