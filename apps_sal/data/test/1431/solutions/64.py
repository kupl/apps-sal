# 1からNまでの数字それぞれの約数を求める
# Nから(大きい値から)見ていき、1であれば入れる
# 数字iを入れた場合、iの約数の数を+1
# それぞれの数はdictで保持する

N = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(N)]

ans_num = 0
ans_list = ""
for i in range(N):
    tmp = N - i
    s = 0
    for j in range(tmp, N + 1, tmp):
        s += ans[j - 1]

    if s % 2 != A[tmp - 1]:
        ans[tmp - 1] = 1
        ans_num += 1
        ans_list += str(tmp)
        ans_list += " "


print(ans_num)
print(ans_list[:-1])
