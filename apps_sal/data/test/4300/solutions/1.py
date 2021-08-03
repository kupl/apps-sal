def ans143(N: int, d: str):
    d = list(map(int, d.split()))
    ans_count = 0
    while len(d) >= 2:
        for i in range(len(d) - 1):
            ans_count += d[0] * d[i + 1]
        del d[0]
    return ans_count


N = int(input())
d = input()
print((ans143(N, d)))
