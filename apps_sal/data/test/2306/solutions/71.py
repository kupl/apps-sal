import numpy as np
N = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))
MAX_V = [0]
for (t, v) in zip(T, V):
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
    answer += (REAL_V[i] + REAL_V[i + 1]) * 0.5 / 2
print(answer)
"\ntsum=np.sum(t)\nprint(tsum)\n \nRuisekit=[t[0]]\n \nfor i in range(1,N):\n  Ruisekit.append(t[i]+Ruisekit[i-1])\n  \nprint(Ruisekit)\n \n \n \n \ndownstart=[]\n \nfor i in range(N-1):\n  if v[i]>v[i+1]:\n    downstart.append(t[i]-(v[i]-v[i+1]))\n \nprint(downstart)\n \nvelocity=0\ndownindex=0\n \nif downstart:\n  nextdownstarttime=downstart[downindex]\n \nstate='up'\nupstarttime=0\nupstartspeed=0\nanswer=0\nmaxspeed=v[0]\nmaxspeedindex=0\n \nfor time in range(1,tsum+1):\n  if state=='up':\n    velocity+=1\n    #print('velocity:',velocity)\n    #print('time',time)\n  if state=='down':\n    velocity-=1\n  if time==nextdownstarttime:\n    if state=='plane':\n      answer+=(time-planestarttime)*speed\n    state='down'\n    print(state)\n    downstarttime=time\n    downstartspeed=speed\n    downindex+=1\n    if downindex<len(downstart):\n      nextdownstarttime=downstart[downindex]\n  if time==Ruisekit[maxspeedindex]:\n    maxspeedindex+=1\n    if maxspeedindex<len(v):\n      maxspeed=v[maxspeedindex]\n  if velocity==maxspeed and state!='plane':\n    if state=='up':\n      answer+=(time-upstarttime)*(velocity-upstartspeed)*0.5\n      answer+=(time-upstarttime)*upstartspeed\n    if state=='down':\n      answer+=(time-downstarttime)*(downstartspeed-velocity)*0.5\n      answer+=(time-downstarttime)*downstartspeed\n    \n    state='plane'\n    planestarttime=time\n    speed=velocity\n    \n  print(answer,time,maxspeed,velocity,state)\n"
