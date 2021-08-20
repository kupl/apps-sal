arr = input()
(N, B) = [int(x) for x in arr.split(' ')]
arr = input()
A = [int(x) for x in arr.split(' ')]
base = []
for i in range(B):
    arr = input()
    (H, G) = [int(x) for x in arr.split(' ')]
    base.append([H, G])
base.sort()
idx = sorted(range(len(A)), key=lambda k: A[k])
A.sort()
s = 0
k = -1
ans = [0] * N
for i in range(N):
    attack = A[i]
    while k < B - 1:
        if base[k + 1][0] <= attack:
            s += base[k + 1][1]
            k += 1
        else:
            break
    ans[idx[i]] = s
for num in ans:
    print(num, end=' ')
