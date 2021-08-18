
A = list(input())
n = len(A)
mod = 10**9 + 7
ans = 0
numa = A[0] == "A"
numa_ = A[0] == "?"
numc = A[2:].count("C")
numc_ = A[2:].count("?")

for i in range(1, n - 1):
    apro = cpro = 0
    if A[i] == "B" or A[i] == "?":
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
