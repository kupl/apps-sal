# https://atcoder.jp/contests/abc089/tasks/abc089_b
S_list = [input() for i in range(2)]
N = map(int, S_list[0].split())
A_list = set(S_list[1].split())
four = {"P", "W", "G", "Y"}
if len(A_list & four) == 3:
    result = "Three"
else:
    result = "Four"
print(result)
