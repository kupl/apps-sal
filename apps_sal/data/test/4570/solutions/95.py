# https://atcoder.jp/contests/abc080/tasks/abc080_a
S_list = list(map(int, input().split()))
N, A, B = S_list
if N * A > B:
    result = B
else:
    result = N * A
print(result)
