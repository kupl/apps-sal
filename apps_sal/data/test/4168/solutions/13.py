N = int(input())
def solve(N):
    if N == 0:
        return '0'
    ans = ''
    while N != 0:
        ans += str(N & 1)
        N >>= 1
        N *= -1
    return ans[::-1]
print(solve(N))
