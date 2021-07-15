from collections import defaultdict
def solve():
  H, W, M = list(map(int, input().split()))
  bomb = defaultdict(lambda: 0)
  lis_h = [0]*H
  lis_w = [0]*W
  for _ in range(M):
    h,w = list(map(int, input().split()))
    h -= 1
    w -= 1
    bomb[(h,w)] = 1
    lis_h[h] += 1
    lis_w[w] += 1
  m_h = max(lis_h)
  m_w = max(lis_w)
  m_h_lis = []
  m_w_lis = []
  for i in range(H):
    if lis_h[i]==m_h:
      m_h_lis.append(i)
  for i in range(W):
    if lis_w[i]==m_w:
      m_w_lis.append(i)
  ans = 0
  for h in m_h_lis:
    for w in m_w_lis:
      if bomb[(h,w)]==0:
        return m_h+m_w
  return m_h+m_w-1
print((solve()))

