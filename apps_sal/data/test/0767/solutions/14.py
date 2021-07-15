N, Z = list(map(int, input().split()))
X = list(map(int, input().split()))
X.sort()

def compute(x1, x2):
    count = 0
    i = 0
    j = 0
    while i < len(x1) and j < len(x2):
        while x2[j] - x1[i] < Z:
            j += 1
            if j == len(x2):
                return count
        count += 1
        i += 1
        j += 1
    return count

if N % 2 == 0:
    print(compute(X[0:N//2], X[N//2:]))
else:
    v1 = compute(X[0: N // 2], X[N // 2:])
    v2 = compute(X[0: N // 2 + 1], X[N // 2 + 1:])
    print(max(v1, v2))

