"""
q, r = divmod(a, k)として、floor(r/(q+1))回まではq=a//kのまま->まとめて引く
"""
def f(a, k):
    while a >= k and a%k:
        q, r = divmod(a, k)
        a -= (r+q)//(q+1)*(q+1)
    if a < k:
        return 0
    return a//k
x = 0
n = int(input())
for _ in range(n):
    a, k = map(int, input().split())
    x ^= f(a, k)
if x:
    print("Takahashi")
else:
    print("Aoki")
