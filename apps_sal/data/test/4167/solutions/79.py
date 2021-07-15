#プログラミング日記   一寸先は闇が人生
# https://pyteyon.hatenablog.com/entry/2018/09/02/094228
# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
N,K = map(int, input().split())

# 偶数、奇数共に
# a,b,c mod 0,0,0 ⇒Kの倍数
multip_K =[i for i in range(K,N+1,K)]

#multip_Kから３つ選び並べる順列組み合わせ
le =len(multip_K)
ans_mod_0 =le **3

# 偶数のみ
# a,b,c mod K/2,K/2,K/2 
ans_mod_haf =0
if K%2 ==0:
    multip_haf =[i for i in range(1,N+1) if i %K ==K//2 ]
    le_haf =len(multip_haf)
    ans_mod_haf =le_haf **3

ans =ans_mod_0 +ans_mod_haf
print(ans)
