# 決め打ち二分探索
# 全員にBダメージ、その後1体選んで(A-B)ダメージと読み替える（対称性の確保。lesson.md参照）
# あとはk回以下で倒せるかを計算して二分探索
# Gluttonyと同様の構造なので、あちらと同様にTLEには注意して書くこと

n, a, b =list(map(int, input().split()))
hitpoints = [int(input()) for _ in range(n)]

additional = a - b

def feasible(k):
    additional_num = sum([max((hp-(b*k) + additional - 1) // additional, 0) for hp in hitpoints])
    return additional_num <= k

ok = 10**9+1
ng = 0

# めぐる式二分探索
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if feasible(mid):
        ok = mid
    else:
        ng = mid

print(ok)

