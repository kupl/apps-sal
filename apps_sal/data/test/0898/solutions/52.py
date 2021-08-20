import math
(N, M) = map(int, input().split())
l = []
for i in range(1, int(math.sqrt(M)) + 1):
    if M % i == 0:
        l.append(i)
        if i != M // i:
            l.append(M // i)
l.sort(reverse=True)
for n in l:
    if n * N <= M:
        ans = n
        break
print(ans)
