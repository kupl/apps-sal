import numpy as np

N = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))

MAX_V = [0]
for t, v in zip(T, V):
    MAX_V[-1] = min(MAX_V[-1], v)
    for _ in range(t * 2):
        MAX_V.append(v)

timelistsize = len(MAX_V)
REAL_V = [0] * timelistsize

for i in range(1, timelistsize):
    REAL_V[i] = min(REAL_V[i - 1] + 0.5, MAX_V[i])

REAL_V[-1] = 0
for i in range(timelistsize - 1, 0, -1):
    REAL_V[i - 1] = min(REAL_V[i] + 0.5, REAL_V[i - 1])


answer = 0
for i in range(timelistsize - 1):
    answer += ((REAL_V[i] + REAL_V[i + 1]) * 0.5 / 2)
print(answer)

'''
tsum=np.sum(t)
print(tsum)
 
Ruisekit=[t[0]]
 
for i in range(1,N):
  Ruisekit.append(t[i]+Ruisekit[i-1])
  
print(Ruisekit)
 
 
 
 
downstart=[]
 
for i in range(N-1):
  if v[i]>v[i+1]:
    downstart.append(t[i]-(v[i]-v[i+1]))
 
print(downstart)
 
velocity=0
downindex=0
 
if downstart:
  nextdownstarttime=downstart[downindex]
 
state='up'
upstarttime=0
upstartspeed=0
answer=0
maxspeed=v[0]
maxspeedindex=0
 
for time in range(1,tsum+1):
  if state=='up':
    velocity+=1
  if state=='down':
    velocity-=1
  if time==nextdownstarttime:
    if state=='plane':
      answer+=(time-planestarttime)*speed
    state='down'
    print(state)
    downstarttime=time
    downstartspeed=speed
    downindex+=1
    if downindex<len(downstart):
      nextdownstarttime=downstart[downindex]
  if time==Ruisekit[maxspeedindex]:
    maxspeedindex+=1
    if maxspeedindex<len(v):
      maxspeed=v[maxspeedindex]
  if velocity==maxspeed and state!='plane':
    if state=='up':
      answer+=(time-upstarttime)*(velocity-upstartspeed)*0.5
      answer+=(time-upstarttime)*upstartspeed
    if state=='down':
      answer+=(time-downstarttime)*(downstartspeed-velocity)*0.5
      answer+=(time-downstarttime)*downstartspeed
    
    state='plane'
    planestarttime=time
    speed=velocity
    
  print(answer,time,maxspeed,velocity,state)
'''
