from sys import stdin, stdout

MOD = 998244353

def __starting_point():
    n = int(stdin.readline())
    A = [int(x) for x in stdin.readline().rstrip().split()]
    B = [int(x) for x in stdin.readline().rstrip().split()]

    for i, a in enumerate(A):
        A[i] *= (i+1)*(n-i)

    A.sort(reverse = True)
    B.sort()

    res = 0
    for a, b in zip(A, B):
        res += a * b
        res %= MOD
    
    print(res)

__starting_point()
