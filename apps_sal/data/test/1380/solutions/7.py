def check_bounds(start):
    return heights[start]-start*k >= 1

n,k = list(map(int,input().split()))
heights = list(map(int,input().split()))
seq_start = -1
lon_seq = [0]*n
max_len = 0
cur_seq= [0]*n
cur_len=0
for i,a in enumerate(heights):
    cur_seq=[0]*n
    cur_len=0
    if check_bounds(i):
        for j,b in enumerate(heights):
            if b == a+(j-i)*k:
                cur_seq[j]=1
                cur_len+=1
        if cur_len>max_len:
            lon_seq=cur_seq
            max_len=cur_len
            seq_start=i
print(n-max_len)
for i,a in enumerate(heights):
    if lon_seq[i] != 1:
       diff=a-(heights[seq_start]+(i-seq_start)*k)
       if diff>0:
           print('{0} {1} {2}'.format('-',i+1,abs(diff)))
       else:
           print('{0} {1} {2}'.format('+',i+1,abs(diff)))


