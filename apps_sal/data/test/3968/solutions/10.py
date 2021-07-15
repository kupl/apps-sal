import sys
import copy

line = sys.stdin.readline().strip('\n')
line = sys.stdin.readline().strip('\n')
nums = list(map(int, line.split()))

def primes():
    prim = [1 for i in range(0,400000)]
    prim[1] = 0
    prim[2] = 1
    for i in range(2,400000):
        if(prim[i] == 1):
            tmp = i
            while(tmp+i<400000):
                tmp+=i
                prim[tmp] = 0   
    return prim

ps = primes()
cnt1 = 0
for i in range(len(nums)):
    if(nums[i] == 1):
        cnt1+=1
cnt2 = len(nums)-cnt1
cnt = 0
for i in range(len(nums)):
    if(ps[cnt+1] == 1 and cnt1>0):
        cnt+=1
        cnt1-=1
        print(1, end=' ')
    elif(cnt2>0):
        cnt2-=1
        cnt+=2
        print(2, end=' ')
    else:
        cnt1-=1
        print(1, end=' ')
