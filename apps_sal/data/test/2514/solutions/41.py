from collections import Counter

n = int(input())
a = list(map(int, input().split()))
q = int(input())

counter = Counter(a)
sum_res = sum(a)  # はじめの合計、名前がsumだとsum関数とかぶってよくないので

# q回操作します。ループ変数は使わないので_とします（Pythonの慣習）
for _ in range(q):
    before, after = map(int, input().split())

    # 合計を変更します
    sum_res -= before * counter[before]
    sum_res += after * counter[before]

    # 個数を変更します
    counter[after] += counter[before]
    counter[before] = 0

    print(sum_res)
