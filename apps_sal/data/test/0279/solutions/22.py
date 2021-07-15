v1, v2 = list(map(int, input().split()))
t, d = list(map(int, input().split()))

if v1 > v2:
    v1, v2 = v2, v1

if d == 0:
    print(t * v1)
else:
    a = [i for i in range(v1, v1 + t * d, d)]
    b = [i for i in range(v2, v2 + t * d, d)]
    b.reverse()
    i = 0
    answer = 0
    while i < t - 1:
        if abs(a[i] - b[i + 1]) <= d:
            if sum(a[:i + 1]) + sum(b[i + 1:]) > answer:
                answer = sum(a[:i + 1]) + sum(b[i + 1:])
        i += 1
    print(answer)

