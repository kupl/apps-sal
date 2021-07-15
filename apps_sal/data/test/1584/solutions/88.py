import bisect

N = int(input())
L_list = list(map(int, input().split()))

L_list_min = sorted(L_list)
ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        #min = isect.bisect_left(L_list_min, L_list_min[j]+1)
        min = j+1
        max = bisect.bisect_left(L_list_min, L_list_min[i]+L_list_min[j])
        #print(i, j, max, min)
        if max - min >= 0:
            ans += max - min
        
print(ans)
