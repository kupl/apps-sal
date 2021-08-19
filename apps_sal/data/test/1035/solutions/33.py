import math
A, B = map(int, input().split())
C = math.gcd(A, B)

# N以下の素数れっきょエラトステネス


def prime(N):
    lsprime = [0, 0] + [1 for i in range(N - 1)]
    lsprime2 = []
    for i in range(N + 1):
        if lsprime[i] == 0:
            continue
        lsprime2.append(i)
        k = i
        while i <= N:
            lsprime[i] = 0
            i += k
    return lsprime2

# 素因数分解


def prime2(N):
    arr = []
    temp = N
    setprime = set()
    for i in range(2, int(-(-N**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            setprime.add(i)
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
        setprime.add(temp)

    if arr == []:
        arr.append([N, 1])

    return arr, setprime


_, setp = prime2(C)
print(len(setp) + 1)
