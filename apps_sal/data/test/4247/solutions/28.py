N = int(input())
P = list(map(int, input().split()))
cnt = 0
for i in range(1, N - 1):
    l = [P[i - 1], P[i], P[i + 1]]
    l.sort()
    if l[1] == P[i]:
        cnt += 1
print(cnt)
