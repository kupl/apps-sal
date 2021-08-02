# https://atcoder.jp/contests/abc117/tasks/abc117_b
S_list = [input() for i in range(2)]
N = map(int, S_list[0].split())
L_list = list(map(int, S_list[1].split()))

if sum(L_list) > max(L_list) * 2:
    result = "Yes"
else:
    result = "No"
print(result)
