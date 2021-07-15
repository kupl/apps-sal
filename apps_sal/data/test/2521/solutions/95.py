import heapq


def solve(n):
  a = list(map(int,input().split()))
  # 左半分を計算して右端[n+idx]でメモ
  # 左半分は最大化したいので最小値が初めに出てくるようにする
  leftHsum = [0 for i in range(n+1)]
  leftH = a[0:n]
  heapq.heapify(leftH)
  leftHsum[0] = sum(leftH) # 
  for i in range(n):
    if leftH[0] < a[n+i]:
      leftHsum[i+1] = leftHsum[i] - leftH[0] + a[n+i]
      heapq.heappop(leftH)
      heapq.heappush(leftH, a[n+i])
    else:
      leftHsum[i+1] = leftHsum[i]
  # 右半分は負の値で保持する
  # もっとも大きい値から追い出していく
  rightHsum = [0 for i in range(n+1)]
  rightH = list([-x for x in a[2*n:3*n]])
  heapq.heapify(rightH)
  rightHsum[0] = - sum(rightH)
  for i in range(n):
    if rightH[0] < -a[2*n-i-1]:
      rightHsum[i+1] = rightHsum[i] + rightH[0] + a[2*n-i-1]
      heapq.heappop(rightH)
      heapq.heappush(rightH, -a[2*n-i-1])
    else:
      rightHsum[i+1] = rightHsum[i]
  result = -1000000000000000000
  #print(leftHsum)
  #print(rightHsum)
  for i in range(n+1):
    result = max(result, leftHsum[0+i]-rightHsum[n-i])
  return result





n = int(input())
print((solve(n)))

