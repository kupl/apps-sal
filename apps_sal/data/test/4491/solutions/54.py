N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
a1 = [0]
a2 = [0]
for i in range(N):
    if i == 0:
        a1.append(A1[i])
        a2.append(A2[i])
    else:
        a1.append(a1[-1] + A1[i])
        a2.append(a2[-1] + A2[i])
ans = 0
for i in range(N):
    if a1[i + 1] + a2[-1] - a2[i] > ans:
        ans = a1[i + 1] + a2[-1] - a2[i]
print(ans)
