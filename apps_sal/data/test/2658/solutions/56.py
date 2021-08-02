N, K = map(int, input().split())
A = list(map(int, input().split()))

count = [-1] * (N + 1)  # その点へ最初に到達した回
pos = 1  # 現在地
num = 0  # 試行回数
while count[pos] == -1:
    count[pos] = num
    pos = A[pos - 1]
    num += 1

loop = max(count) - count[pos] + 1

if num > K:
    print(count.index(K))
elif loop == 1 and num <= K:
    print(count.index(max(count)))
else:
    start = num - loop
    ans = (K - num) % loop
    print(count.index(start + ans))
