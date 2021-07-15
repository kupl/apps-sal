import heapq


class DeletableHeap:
  def __init__(self, reversed=False, debug=False):
    self.heap = []
    self.removed = {}
    self.reversed = reversed  # get the max if True
    self.factor = -1 if reversed else 1
    self.debug = debug
  
  def push(self,x):
#    if self.debug: print('push', x, self.heap, self.removed)
    heapq.heappush(self.heap, x * self.factor)
  
  def pop(self):
#    if self.debug: print('pop', self.heap, self.removed)
    while self.heap:
      a = heapq.heappop(self.heap) * self.factor
      if a in self.removed and self.removed[a]:
        self.removed[a] -= 1
        if self.removed[a] == 0:
          del self.removed[a]
      else:
 #       if self.debug: print(a)
        return a

  def peek(self):
 #   if self.debug: print('peek', self.heap, self.removed)
    while self.heap:
      a = self.heap[0] * self.factor
      if a in self.removed and self.removed[a]:
        self.removed[a] -= 1
        if self.removed[a] == 0:
          del self.removed[a]
        heapq.heappop(self.heap)
      else:
 #       if self.debug: print(a)
        return a

  def remove(self,x):
  #  if self.debug: print('remove', x, self.heap, self.removed)
    if x not in self.removed:
      self.removed[x] = 0
    self.removed[x] += 1
    
N, Q = list(map(int, input().split()))

KG = [DeletableHeap(reversed=True) for _ in range(2*10**5)]
B = []
A = []
for _ in range(N):
  a, b = list(map(int, input().split()))
  b -= 1
  KG[b].push(a)
  B.append(b)
  A.append(a)

rates = DeletableHeap(debug=False)
for kg in KG:
  if kg.peek() is not None:
    rates.push(kg.peek())
#print(rates.heap, rates.removed)
    
for _ in range(Q):
#  print('######')
  c, d = list(map(int, input().split()))
  c -= 1
  d -= 1
  # c is at B[c]
  b = B[c]
  B[c] = d
  a = A[c] # rate
  # c moves from b to d
  rates.remove(KG[b].peek())
  KG[b].remove(a)
  if KG[b].peek() is not None:
    rates.push(KG[b].peek())
  
  if KG[d].peek() is not None:
    rates.remove(KG[d].peek())
  KG[d].push(a)
  rates.push(KG[d].peek())
  #print(rates.heap, rates.removed)
  print((rates.peek()))
  
 # for i in range(10):
 #   print('kg', i, KG[i].heap, KG[i].removed)



