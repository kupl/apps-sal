n, m = map(int, input().split())
xyz = [list(map(int, input().split())) for i in range(n)]
l1, l2, l3, l4, l5, l6, l7, l8 = sorted(xyz, key=lambda x: x[0] + x[1] + x[2], reverse=True), sorted(xyz, key=lambda x: x[0] + x[1] - x[2], reverse=True), sorted(xyz, key=lambda x: x[0] - x[1] + x[2], reverse=True), sorted(xyz, key=lambda x: x[0] - x[1] - x[2], reverse=True), sorted(xyz, key=lambda x: -(x[0]) + x[1] + x[2], reverse=True), sorted(xyz, key=lambda x: -(x[0]) + x[1] - x[2], reverse=True), sorted(xyz, key=lambda x: -(x[0]) - x[1] + x[2], reverse=True), sorted(xyz, key=lambda x: -(x[0]) - x[1] - x[2], reverse=True)


def sum2(l):
    ans = 0
    cnt = 0
    for i in l:
        cnt += i[0]
    ans += abs(cnt)
    cnt = 0
    for i in l:
        cnt += i[1]
    ans += abs(cnt)
    cnt = 0
    for i in l:
        cnt += i[2]
    ans += abs(cnt)
    return ans


print(max(sum2(l1[:m]), sum2(l2[:m]), sum2(l3[:m]), sum2(l4[:m]), sum2(l5[:m]), sum2(l6[:m]), sum2(l7[:m]), sum2(l8[:m]),))
