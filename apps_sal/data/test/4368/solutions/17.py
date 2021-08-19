# https://atcoder.jp/contests/abc156/tasks/abc156_b
N, K = map(int, input().split())
q, mod = divmod(N, K)
mod_list = [mod]
while True:
    q, mod = divmod(q, K)
    mod_list.append(mod)
    if q <= 0:
        break

n_ary = int("".join(map(str, mod_list[::-1])))
print(len(str(n_ary)))
