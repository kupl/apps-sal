N = int(input())
len = list(map(int, input().split()))

# 定理 : 一番長い辺が他の N−1 辺の長さの合計よりも真に短い場合に限り、条件を満たすN角形が描ける。
# 条件を満たすN角形が描けるなら Yes、そうでないなら No を出力せよ。

short_len = sum(len) - max(len)
result = 'Yes' if short_len > max(len) else 'No'
print(result)
