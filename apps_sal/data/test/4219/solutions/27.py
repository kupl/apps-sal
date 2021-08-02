N = int(input())
testimonies = []

for i in range(N):
    A = int(input())
    testimony = []
    for j in range(A):
        testimony.append(list(map(int, input().split())))
        testimony[-1][0] -= 1
    testimonies.append(testimony)

ans = 0
for i in range(2**N):
    isContradiction = False
    for j in range(N):
        if not i & 1 << j: continue
        for x, y in testimonies[j]:
            if i & 1 << x: x = 1
            else: x = 0
            if not x == y:
                isContradiction = True
                break
    if not isContradiction:
        ans = max(ans, bin(i).count("1"))
print(ans)
