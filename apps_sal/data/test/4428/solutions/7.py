n = int(input())
D = list(map(int, input().split()))
sums1, sums2 = {}, {}

s = 0
for i, d in enumerate(D):
    s += d
    if s not in sums1:
        sums1[s] = i

s = 0
for i, d in enumerate(D[::-1]):
    s += d
    if s not in sums2:
        sums2[s] = i

sums1 = sorted(list(sums1.items()), reverse=True)
answer = 0
for s, i in sums1:
    if s in sums2 and sums2[s] + i + 2 <= n:
        answer = s
        break
print(answer)
