n = int(input())
t = [0] + list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
(res, cnt) = ([], [0] * (n + 1))
for i in a:
    cnt[i] += 1
for i in range(1, n + 1):
    if t[i] == 0:
        continue
    curr_res = [i]
    x = a[i]
    while cnt[x] == 1:
        curr_res.append(x)
        x = a[x]
    if len(curr_res) > len(res):
        res = curr_res[:]
res.reverse()
print(len(res))
print(*res)
