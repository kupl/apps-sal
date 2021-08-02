N = int(input())

BA = []
for i in range(N):
    A, B = map(int, input().split())
    BA.append([B, A])

BA.sort()

check = True
sum_A = 0
for j in range(N):
    sum_A += BA[j][1]
    if sum_A > BA[j][0]:
        check = False
        break

print("Yes" if check else "No")
