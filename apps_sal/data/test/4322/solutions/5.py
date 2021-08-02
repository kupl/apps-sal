n = int(input())
a = list(map(int, input().split()))
cnt = [0] * (200005)
for i in range(0, n):
    cnt[a[i]] += 1
ans = 0
ansl = 0
ansr = 0
l = 1
N = 200001
while (l <= N):
    if cnt[l] == 0:
        l += 1
    else:
        r = l
        now = 0
        while (r <= N):
            if cnt[r] == 0:
                r -= 1
                break
            elif cnt[r] == 1 and l != r:
                now += cnt[r]
                break
            else:
                now += cnt[r]
                r += 1
        if now > ans:
            ansl = l
            ansr = r
            ans = now
        # print(l,r,now)
        if l == r:
            l = r + 1
        else:
            l = r
seq = []
for i in range(ansl, ansr + 1):
    seq.append(i)
    cnt[i] -= 1
for i in range(ansr, ansl - 1, -1):
    while cnt[i] > 0:
        seq.append(i)
        cnt[i] -= 1
print(len(seq))
for i in seq:
    print(i, end=" ")
