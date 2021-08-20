t = int(input())
for i in range(t):
    n = int(input())
    q = list(map(int, input().split()))
    used = {q[0]: True}
    seq = [q[0]]
    ks = 1
    for j in range(1, n):
        if q[j] == q[j - 1]:
            for k in range(ks, q[j]):
                if used.get(k) is None:
                    seq.append(k)
                    used[k] = True
                    ks = k + 1
                    break
            else:
                print(-1)
                break
        else:
            used[q[j]] = True
            seq.append(q[j])
    else:
        print(*seq)
