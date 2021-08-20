"""
中途半端にとく問題は一種類のみで良い。
全探索で全ての点数帯について、ボーナスをとるか・一問もとかないかで全探索
もし点がGに満たない場合は一番点が高いものを解く。
"""
(d, g) = map(int, input().split())
pc = [list(map(int, input().split())) for i in range(d)]
ans = float('inf')
for bit in range(1 << d):
    count = 0
    sum = 0
    rest = list(range(1, d + 1))
    for i in range(d):
        if bit & 1 << i:
            sum += pc[i][0] * (i + 1) * 100 + pc[i][1]
            count += pc[i][0]
            rest.remove(i + 1)
    if sum < g:
        use = max(rest)
        n = min(pc[use - 1][0], -(-(g - sum) // (use * 100)))
        count += n
        sum += n * use * 100
    if sum >= g:
        ans = min(ans, count)
print(ans)
