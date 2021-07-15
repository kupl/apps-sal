N = int(input())
ans = set()

def check(N, k):
    if k<2:
        return False
    N //= k
    while N:
        if (N-1)%k==0:
            return True
        if N%k:
            return False
        N //= k
    return False


for k in range(1, int(N**0.5)+1):
    if (N-1)%k==0:
        k1, k2 = k, (N-1)//k
        ans.add(k1)
        ans.add(k2)
    if N%k==0:
        k1, k2 = k, N//k
        if check(N, k1):
            ans.add(k1)
        if check(N, k2):
            ans.add(k2)

ans.remove(1)
print(len(ans))
