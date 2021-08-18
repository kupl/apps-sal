n = int(input())
a = list(map(int, input().split()))
l1 = [0] * 100001
l2 = [0] * 100001
if a.count(a[0]) == n:
    print((n // 2))
    return

for i in range(0, n, 2):
    l1[a[i]] += 1
for i in range(1, n, 2):
    l2[a[i]] += 1

x, y = max(l1), max(l2)
# print(x,y)
i_x, i_y = l1.index(x), l2.index(y)
# print(i_x,i_y)

L1 = sorted(l1, reverse=True)
L2 = sorted(l2, reverse=True)

if i_x == i_y:
    # 奇数番目を2番目に多い数でそろえる場合
    ans = min(((n // 2 - L1[1]) + (n // 2 - L2[0])), ((n // 2 - L1[0]) + (n // 2 - L2[1])))
else:
    ans = ((n // 2 - L1[0]) + (n // 2 - L2[0]))
print(ans)
