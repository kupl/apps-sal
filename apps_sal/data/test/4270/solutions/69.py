N = int(input())
v = list(map(int, input().split()))

# 昇順にソートすると、最大値を与えるのは以下の操作を行ったとき：
# v_1 = (v_0 + v_1)/2 (v_0は消滅）
# v_2 = (v_1 + V_2)/2 (v_1は消滅)
# v_(N-1) = (v_(N_1) + v_(N-2))/2 (v_(N-2)は消滅)
# 結局、(N-1)番目の素材が残り、その価値はv_(N-1)

v = sorted(v)
for i in range(N-1):
  v[i+1] = (v[i+1]+v[i])/2
  
print(v[N-1])
