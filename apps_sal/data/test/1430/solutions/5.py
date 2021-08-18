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
        now = 1 - now
        cnt = 1
ls.append(cnt)

if len(ls) % 2 == 0:
    ls.append(0)

Add = 2 * k + 1
ans = 0

left = 0
right = 0
tmp = 0

for i in range(0, len(ls), 2):
    nextLeft = i
    nextRight = min(i + Add, len(ls))

    while nextLeft > left:
        tmp -= ls[left]
        left += 1
    while nextRight > right:
        tmp += ls[right]
        right += 1

    ans = max(tmp, ans)

print(ans)
