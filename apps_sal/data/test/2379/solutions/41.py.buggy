n, k, c = map(int, input().split())
s = input()
left = [-1 for _ in range(k)]
right = [-1 for _ in range(k)]

bef = -10 ** 10
cnt = 0
for i, ss in enumerate(s):
    if ss == "o" and i - bef > c:
        if cnt == k:
            return
        left[cnt] = i
        bef = i
        cnt += 1

cnt = 0
bef = -10 ** 10
for i, ss in enumerate(s[::-1]):
    if ss == "o" and i - bef > c:
        if cnt == k:
            return
        right[k - 1 - cnt] = n - 1 - i
        bef = i
        cnt += 1


for ll, rr in zip(left, right):
    if ll == rr:
        print(ll + 1)
