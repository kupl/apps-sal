N, A, B = map(int, input().split())

# プラン 1: T時間駐車した場合、A × T円 が駐車料金となる。
# プラン 2: 駐車した時間に関わらず B円 が駐車料金となる。
# N時間駐車するとき、駐車料金は最小でいくらになるか求めてください。

plan_A = A * N
plan_B = B

print(min(plan_A, plan_B))
