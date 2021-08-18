N = int(input())
L = list(map(int, input().split()))

if N < 3:
    print(0)
    return

L = sorted(L)

res = 0
for k in range(N):
    for j in range(k):
        for i in range(j):
            if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                continue
            if L[i] + L[j] <= L[k]:
                continue
            res += 1
            #print("{} {} {}".format(L[i], L[j], L[k]))

print(res)
