N = int(input())
A = list(map(int, input().split()))
Q = int(input())

cnt_dict = {}

s = sum(A)
ans = []

for item in A:
    if item not in cnt_dict:
        cnt_dict[item] = 0
    cnt_dict[item] += 1

for _ in range(Q):
    b, c = map(int, input().split())

    if b not in cnt_dict:
        cnt_dict[b] = 0
    if c not in cnt_dict:
        cnt_dict[c] = 0

    s -= b * cnt_dict[b]
    s += c * cnt_dict[b]

    cnt_dict[c] += cnt_dict[b]
    cnt_dict[b] = 0

    ans.append(s)

for i in range(Q):
    print(ans[i])
