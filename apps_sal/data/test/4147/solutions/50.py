from functools import lru_cache
N, A, B, C, *L = list(map(int, open(0).read().split()))


@lru_cache(None)
def popcnt(n):
    return bin(n).count('1')


@lru_cache(None)
def synth(bit):
    length = 0
    for i in range(N):
        if bit >> i & 1:
            length += L[i]
    return length


ans = 1 << 60
for bit1 in range(1, 1 << N):
    if popcnt(bit1) >= N-1:
        continue
    length1 = synth(bit1)

    for bit2 in range(1, 1 << N):
        if bit1 & bit2:
            continue
        if popcnt(bit1 | bit2) == N:
            continue
        length2 = synth(bit2)

        for bit3 in range(1, 1 << N):
            if bit1 & bit3 or bit2 & bit3:
                continue

            length3 = synth(bit3)
            c, b, a = sorted([length1, length2, length3])

            cost = 10*(popcnt(bit1 | bit2 | bit3)-3) + abs(C-c) + abs(B-b) + abs(A-a)
            if cost < ans:
                ans = cost

print(ans)

