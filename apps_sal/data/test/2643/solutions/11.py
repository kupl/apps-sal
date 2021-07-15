def main():
    import numpy as np
    k, q = list(map(int, input().split()))
    d = np.array(list(map(int, input().split())), dtype=np.int64)
    nxm = [list(map(int, input().split())) for _ in [0]*q]
    for n, x, m in nxm:
        d2 = np.sum((d[:(n-2) % k+1]-1) % m+1)
        d3 = np.sum((d[(n-2) % k+1:]-1) % m+1)
        print((n-1-(x % m+(d2+d3)*((n-2)//k)+d2)//m))


main()

