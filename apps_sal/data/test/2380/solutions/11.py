N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
BC = []
for _ in range(M):
    b, c = map(int, input().split())
    BC.append((b, c))
BC.sort(key=lambda bc: -bc[1])

i = 0
done = False
for b, c in BC:
    if done:
        break
    for _ in range(b):
        if i < N and A[i] < c:
            A[i] = c
            i += 1
        else:
            done = True
            break
print(sum(A))
