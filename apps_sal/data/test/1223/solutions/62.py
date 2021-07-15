N = int(input())
P = [int(i) for i in input().split(" ")]

# 各数字が何番目に入っているかを保存する
pos = [0] * (N + 1)
for i in range(N):
    pos[P[i]] = i + 1

l = [0]+[i for i in range(N + 1)]
r = [i + 1 for i in range(N + 1)] + [N + 1]

# 1から順番に見ていく
ans = 0
for i in range(1, N + 1):
    idx = pos[i]
    l1, r1 = l[idx], r[idx]
    l2, r2 = l[l1], r[r1]
    ans += i * ((l1 - l2) * (r1 - idx) + (idx - l1) * (r2 - r1))
    l[r1], r[l1] = l1, r1
print(ans)
