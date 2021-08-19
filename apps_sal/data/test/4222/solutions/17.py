N, K = map(int, input().split())
x = [0] * (N + 1)

for i in range(K):
    d = int(input())
    if d > 0:
        a = list(map(int, input().split()))
        for v in a:
            x[v] += 1

# print(a)

c = 0
for i in range(1, N + 1, 1):
    if x[i] == 0:
        c += 1

print(c)
