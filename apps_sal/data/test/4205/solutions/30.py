def inpl(): return list(map(int, input().split()))


N = int(input())
P = inpl()
Q = sorted(P)

for i in range(N):
    for j in range(i, N):
        R = [p for p in P]
        R[i], R[j] = R[j], R[i]
        for k in range(N):
            if R[k] != Q[k]:
                break
        else:
            print("YES")
            return
else:
    print("NO")
