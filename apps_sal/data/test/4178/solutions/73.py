N = int(input())
A = list(map(int,input().split()))
 
# 後ろ向きに考える
# 各要素は基本的に大きくしたいので、そのまま、もしくは
# うまくいかない場合にのみ、1減らす
ans = 'Yes'
for i in range(N-1, 0, -1):
  if A[i] < A[i-1]: A[i-1] -= 1
  if A[i] < A[i-1]:
    ans = 'No'
    break

print(ans)
