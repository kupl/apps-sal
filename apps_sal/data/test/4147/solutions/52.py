import itertools

N, A, B, C = list(map(int, input().split()))

l = [int(input()) for _ in range(N)]

ans = 10**10
# [竹1の選択, 竹2の選択, ..., 竹Nの選択]
# 4**8==65536
for x in itertools.product([0, 1, 2, 3], repeat=N):
    # [不使用の竹の合計長さ、Aに使用する竹の合計長さ、Bに...、Cに...]
    bamboo = [0] * 4
    tmp = 0
    for i in range(N):
        # 始めて選ぶ場合はコストがかからない
        if x[i] in [1, 2, 3] and bamboo[x[i]] > 0:
            tmp += 10
        bamboo[x[i]] += l[i]

    # A,B,Cそれぞれについて、1本以上使う必要がある
    if 0 in bamboo[1:]:
        continue
    # 延長魔法 or 短縮魔法で調整
    tmp += abs(bamboo[1] - A) + abs(bamboo[2] - B) + abs(bamboo[3] - C)

    ans = min(ans, tmp)

print(ans)
