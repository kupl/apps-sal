n,pos,l,r  = [int(i) for i in input().split()]

time_l = 0;
if l != 1:
    time_l += abs(pos - l) + 1 # move to l and delete
    pos1 = l
else:
    pos1 = pos
if r != n: time_l += abs(r-pos1) + 1 # move to r and delete

time_r = 0;
if r != n:
    time_r += abs(pos - r) + 1 # move to l and delete
    pos1 = r
else:
    pos1 = pos
if l != 1: time_r += abs(pos1-l) + 1 # move to r and delete

#print(time_l, time_r)
print(min(time_l, time_r))

