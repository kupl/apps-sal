from sys import stdin
#def read(): return map(int, stdin.readline().split())

n = int(stdin.readline())
a = stdin.readline()
b = stdin.readline()

cnt0 = 0
cnt1 = 0
cnt2 = 0
for i in range(n*2):
  if a[i] == '0':
    if b[i] == '0': cnt0 += 1
    else: cnt1 += 1
  elif b[i] == '0': cnt2 += 1

cnt = [ cnt0, cnt1, cnt2, 2*n - cnt0 - cnt1 - cnt2 ]

dif = 0
iter1 = iter ( ( 0b11, 0b10, 0b01, 0b00 ) )
iter2 = iter ( ( 0b11, 0b01, 0b10, 0b00 ) )
cur1 = next(iter1)
cur2 = next(iter2)
left = n
while left > 0:
  while cnt[cur1] == 0:
    cur1 = next(iter1)
  dif += (cur1>>1)
  cnt[cur1] -= 1
  
  while cnt[cur2] == 0:
    cur2 = next(iter2)  
  dif -= (cur2&1)
  cnt[cur2] -= 1
  
  jump = min ( cnt[cur1], cnt[cur2] ) if cur1 != cur2 else cnt[cur1]//2
  dif += ( (cur1>>1) - (cur2&1) )*jump
  cnt[cur1] -= jump
  cnt[cur2] -= jump
  left -= jump+1
  

if dif > 0: print( "First" )
elif dif < 0: print ( "Second" )
else: print ( "Draw" )

