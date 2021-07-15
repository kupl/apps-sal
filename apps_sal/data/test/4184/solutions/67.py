# B - Balance
# https://atcoder.jp/contests/abc129/tasks/abc129_b

n = int(input())
w = list(map(int, input().split()))

result = sum(w)

for i in range(n):
    wk = abs(sum(w[:i]) - sum(w[i:]))
    if result > wk:
        result = wk

print(result)

