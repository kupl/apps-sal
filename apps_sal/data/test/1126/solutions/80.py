# 参考
# https://atcoder.jp/contests/abc179/submissions/16890682

n, x, m = map(int, input().split())
check = [False] * (10**5 + 10)
check_list = [x]
a = x
# ループを見つける
for i in range(n):
    a = (a * a) % m
    if check[a]:
        break
    check[a] = True
    check_list.append(a)
 
# ループの長さを算出
index = check_list.index(a)
# ループはいる前のやつ
loop_bef = check_list[0:index]
# ループのやつ
loop = check_list[index:]
 
# ループが何周あるのかと，ループ終わりがいくつ要素あるかを計算
loop_num = (n - len(loop_bef)) // len(loop)
after_loop = (n - len(loop_bef)) % len(loop)
 
# ループ前+ループのsum*ループ数+ループ後のsumが答え
ans = sum(loop_bef) + sum(loop) * loop_num + sum(loop[:after_loop])
 
print(ans)
