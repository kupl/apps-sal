
N, M = map(int, input().split())
A = list(map(int, input().split()))
B_C = [list(map(int, input().split())) for _ in range(M)]

B_C = sorted(B_C, reverse=True, key=lambda x: x[1])


cnt = 0
for l in B_C:
    for i in range(l[0]):
        A.append(l[1])
        cnt += 1
        if cnt > N:
            break
    else:
        continue
    break

A = sorted(A, reverse=True)

print(sum(A[:N]))
