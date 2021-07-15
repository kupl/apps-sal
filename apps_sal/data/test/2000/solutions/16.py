n = int(input())
A = list(map(int, input().split()))
cnt = {}

for a in A:
    if a in cnt:
        cnt[a] += 1
    else:
        cnt[a] = 1

c = 0
for a in A:
    cnt[a] -= 1
    for n in range(1, 32):
        if 2**n - a in cnt:
            c += cnt[2**n - a]

print(c)

