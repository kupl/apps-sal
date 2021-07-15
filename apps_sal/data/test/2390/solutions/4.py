from itertools import accumulate
n,c = map(int,input().split())
wv = [[0,0]]+[list(map(int,input().split())) for i in range(n)]+[[c,0]]
n += 2
ansls = []
ls1 = [0]*n
ls2 = [0]*n
ls3 = [0]*n
ls4 = [0]*n
for i in range(1,n):
  w,v = wv[i]
  w -= wv[i-1][0]
  ls1[i] = v-w*2
  ls2[i] = v-w
for i in range(n-2,-1,-1):
  w,v = wv[i]
  w -= wv[i+1][0]
  ls3[n-i-1] = v+w*2
  ls4[n-i-1] = v+w
als1 = list(accumulate(ls1))
als2 = list(accumulate(ls2))
als3 = list(accumulate(ls3))
als4 = list(accumulate(ls4))
als1 = list(accumulate(als1,max))
als2 = list(accumulate(als2,max))
als3 = list(accumulate(als3,max))
als4 = list(accumulate(als4,max))
for i in range(n-1):
  ansls.append(als1[i]+als4[n-2-i])
  ansls.append(als2[i]+als3[n-2-i])
print(max(ansls))
