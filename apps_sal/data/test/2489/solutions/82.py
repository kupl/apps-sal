N = int(input())
A = list(map(int, input().split()))
max_a = max(A) + 1
counter = [0 for _ in range(max_a)]

for i in A:
    for j in range(i, max_a, i):
        counter[j] += 1

res = 0

for a in A:
    if counter[a] == 1:
        res += 1

print(res)
