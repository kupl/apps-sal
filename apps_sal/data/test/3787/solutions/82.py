N, A, B = list(map(int, input().split()))

base = list(range(N, 0, -1))
if A < B:
    tmp = A
    A = B
    B = tmp
    base.reverse()

if (N - 1) // B + 1 <= A <= N - B + 1:
    possible = 1
else:
    possible = 0

if possible:
    split = [A]
    N_left = N - A
    for i in range(B-1, 0, -1):
        split.append((N_left - 1) // i + 1 + split[-1])
        N_left -= (N_left - 1) // i + 1

    split.insert(0, 0)
    ans = []
    for i in range(1, len(split)):
        rev = base[split[i-1]:split[i]]
        rev.reverse()
        ans.extend(rev)
    print((" ".join(map(str, ans))))
else:
    print((-1))

