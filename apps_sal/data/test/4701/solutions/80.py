from functools import reduce

def operator(x, K, N):
    res = (lambda x: 2*x if x < K else x+K)(x)
    return res if N == 1 else operator(res, K, N-1)

def main():
    with open(0) as f:
        N, K = list(map(int, f.read().split()))
    ans = operator(1, K, N)
    print(ans)

main()    

