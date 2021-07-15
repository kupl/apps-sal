# coding: utf-8
# Your code here!
N,C=map(int,input().split())

sushi=[]
for _ in range(N):
    x,v=map(int,input().split())
    sushi.append([x,v])

sushi_2=list(map(lambda x:[x[0]+C, x[1]] , sushi))

sushi+=sushi_2

cal=[[0,0] for i in range(2*N)]

pre_x=C
for i in range(N, 2*N):
    x, v = sushi[i][0], sushi[i][1]
    cal[i][0], cal[i][1] = v-(x-pre_x), v-2*(x-pre_x)
    pre_x=x


pre_x=C
for i in range(N)[::-1]:
    x, v = sushi[i][0], sushi[i][1]
    cal[i][0], cal[i][1] = v-(pre_x-x), v-2*(pre_x-x)
    pre_x=x

left=[[0,0] for i in range(N)]
right=[[0,0] for i in range(N)]

temp_0,temp_1=cal[N][0],cal[N][1]
right[0][0], right[0][1] = max(0,temp_0), max(0,temp_1)
for i in range(N+1,2*N):
    temp_0+=cal[i][0]
    temp_1+=cal[i][1]
    right[i-N][0], right[i-N][1] = max(right[i-N-1][0],temp_0), max(right[i-N-1][1],temp_1)

temp_0,temp_1=cal[N][0],cal[N][1]
right[0][0], right[0][1] = max(0,temp_0), max(0,temp_1)
for i in range(N+1,2*N):
    temp_0+=cal[i][0]
    temp_1+=cal[i][1]
    right[i-N][0], right[i-N][1] = max(right[i-N-1][0],temp_0), max(right[i-N-1][1],temp_1)

temp_0, temp_1=cal[N-1][0], cal[N-1][1]
left[-1][0], left[-1][1] = max(0,temp_0), max(0,temp_1)
for i in range(N-1)[::-1]:
    temp_0+=cal[i][0]
    temp_1+=cal[i][1]
    left[i-N][0], left[i-N][1] = max(left[i-N+1][0],temp_0), max(left[i-N+1][1],temp_1)

"""
print(sushi)
print(cal)
print(right)
print(left)
"""

ans=max(left[0][0],0)
for i in range(1,N):
    ans=max(ans,left[i][0]+right[i-1][1])

ans=max(right[N-1][0],ans)
for i in range(N-1)[::-1]:
    ans=max(ans,right[i][0]+left[i+1][1])


print(ans)
