n, k = map(int, input().split())
S = list(input())

if "0" not in S:
    print(n)
    return

# 1の個数、0の個数、1の個数、、、
cnt = []

# 先頭が0なら1が0個とみなす
if S[0] == "0":
    cnt.append(0)

# 個数勘定
i = 0
while i < n:
    j = i
    while j < n and S[i] == S[j]:
        j += 1
    cnt.append(j-i)
    i = j

# 最後尾が0なら1が0個とみなす
if S[-1] == "0":
    cnt.append(0)

# cnt の累積和
cumCnt = [0]
for c in cnt:
    cumCnt.append(cumCnt[-1] + c)

# print(cnt)
# print(cumCnt)

lenCnt = len(cnt)
lenCumCnt = len(cumCnt)
ans = 0

for left in range(0, lenCumCnt, 2):
    right = min(left + 2*k+1, lenCumCnt-1)
    ans = max(ans, cumCnt[right] - cumCnt[left])
print(ans)
