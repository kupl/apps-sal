# B - 754
# https://atcoder.jp/contests/abc114/tasks/abc114_b

s = input()

result = 753

for i in range(len(s) - 2):
    wk = abs(753 - int(s[i:i + 3]))
    if result > wk:
        result = wk

print(result)
