a = int(input())
N = list(input())
f = list(map(int, input().split()))

ind = 0

for i, n in enumerate(N):
    if int(n) < f[int(n) - 1]:
        N[i] = f[int(n) - 1]
        ind = 1
    if int(n) > f[int(n) - 1] and ind == 1:
        break

print("".join(list(map(str, N))))
        

