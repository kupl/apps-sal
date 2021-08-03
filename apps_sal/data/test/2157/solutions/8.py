N, Q = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

count = [0 for i in range(N + 1)]

for q in range(Q):
    l, r = map(int, input().split())
    count[l - 1] += 1
    count[r] -= 1

for i in range(1, N):
    count[i] += count[i - 1]
count.sort()

res = 0
for i in range(N):
    res += count[i + 1] * array[i]

print(res)
