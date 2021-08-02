n, k = map(int, input().split())
s = input()
ls = []

now = 1
cnt = 0
for ele in s:
    if int(ele) == now:
        cnt += 1
    else:
        ls.append(cnt)
        now = 1 - now  # 1と0の切替
        cnt = 1
ls.append(cnt)

# 1-0-1-0-1が欲しい
# 1-0-1-0の場合、1の場合を足す
if len(ls) % 2 == 0:
    ls.append(0)

Add = 2 * k + 1  # [left, right)
ans = 0

left = 0
right = 0
tmp = 0  # [left, right)のsum

# print(ls)
# 1-0-1-0..の１から始める
for i in range(0, len(ls), 2):
    nextLeft = i
    nextRight = min(i + Add, len(ls))
    # print(" value", tmp)
    # print(" p left ", left)
    # print(" p right", right)

    while nextLeft > left:
        # print("left  point, value", left, tmp)
        tmp -= ls[left]
        left += 1
    while nextRight > right:
        # print("right point, value", right, tmp)
        tmp += ls[right]
        right += 1

    ans = max(tmp, ans)
    # print("ans",ans)
    # print("\n")

print(ans)
