# def C(n, r ,mod=10**9+7):
#     if n-r<r: r=n-r
#     if r == 0: return 1
#     if r == 1: return n
#
#     numerator = [n - r + k + 1 for k in range(r)]
#     denominator = [k + 1 for k in range(r)]
#
#     for p in range(2,r+1):
#         pivot = denominator[p - 1]
#         if pivot > 1:
#             offset = (n - r) % p
#             for k in range(p-1,r,p):
#                 numerator[k - offset] /= pivot
#                 denominator[k] /= pivot
#
#     result = 1
#     for k in range(r):
#         if numerator[k] > 1:
#             result *= int(numerator[k]) %mod
#
#     return result % mod

A = list(input())
n = len(A)
mod = 10**9 + 7
ans = 0
numa = A[0] == "A"
numa_ = A[0] == "?"
numc = A[2:].count("C")
numc_ = A[2:].count("?")

for i in range(1, n - 1):
    # print(numa,numa_,numc,numc_)
    apro = cpro = 0
    if A[i] == "B" or A[i] == "?":
        # for k in range(numa_+1):
        #     apro+= (((C(numa_,k)*pow(2,numa_-k,mod))%mod)*(numa+k))%mod
        # for k in range(numc_+1):
        #     cpro+= (((C(numc_,k)*pow(2,numc_-k,mod))%mod)*(numc+k))%mod
        # print(apro,cpro)
        apro = ((3 * numa + numa_) * pow(3, (numa_ - 1), mod)) % mod
        cpro = ((3 * numc + numc_) * pow(3, (numc_ - 1), mod)) % mod
        ans += (apro * cpro) % mod
        ans %= mod
    if A[i] == "A":
        numa += 1
    if A[i] == "?":
        numa_ += 1
    if A[i + 1] == "C":
        numc -= 1
    if A[i + 1] == "?":
        numc_ -= 1
print(ans)
