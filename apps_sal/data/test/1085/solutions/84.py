N = int(input())


def yakusu(N):
    ret = [[], []]
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            ret[0].append(i)
            if i ** 2 != N:
                ret[1].append(N // i)
    return ret[0] + ret[1][::-1]


ans = 0
for a in yakusu(N):
    if a == 1:
        continue

    if N % a == 0:
        b = N
        while b % a == 0:
            b //= a
        if (b - 1) % a == 0:
            ans += 1
print(ans + len(yakusu(N - 1)) - 1)
