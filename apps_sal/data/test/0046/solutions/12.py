n,m = list(map(int,input().split()))
left_first = [n//5]*5
left_second = [m//5]*5
for i in range(n%5):
    left_first[i]+=1
    
for j in range(m%5):
    left_second[j]+=1

ans = left_first[-1]*left_second[-1]
for i in range(4):
    ans+=left_first[i]*left_second[3-i]
    #print(ans)
#print(left_first,left_second)
print(ans)

