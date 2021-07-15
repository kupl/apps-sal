q=int(input())

num_cnt=[[0,0]]
for i in range(1,22000):
    if i<10: num_cnt.append([num_cnt[-1][1]+1,num_cnt[-1][1]+i])
    elif i<100: num_cnt.append([num_cnt[-1][1]+1,num_cnt[-1][1]+9+(i-9)*2])
    elif i<1000: num_cnt.append([num_cnt[-1][1]+1,num_cnt[-1][1]+9+90*2+(i-99)*3])
    elif i<10000: num_cnt.append([num_cnt[-1][1]+1,num_cnt[-1][1]+9+90*2+900*3+(i-999)*4])
    elif i<100000: num_cnt.append([num_cnt[-1][1]+1,num_cnt[-1][1]+9+90*2+900*3+9000*4+(i-9999)*5])

for i in range(q):
    k=int(input())
    left,right=1,len(num_cnt)
    mid=0
    while left<=right:
        mid=(left+right)//2
        if k >= num_cnt[mid][0] and k <= num_cnt[mid][1]:
            break
        if k < num_cnt[mid][0]:
            right=mid-1
        else:
            left=mid+1

    now_cnt=num_cnt[mid][0]-1
    now_val=1
    succ=False
    while not succ:
        temp_val=list(str(now_val))
        for j in temp_val:
            now_cnt+=1
            if now_cnt==k:
                print(j)
                succ=True
                break
        now_val+=1
