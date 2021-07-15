n , k = list(map(int , input().split()))
ques = []
last = [-1]*(n+2)
last[0] = 10000000
last[n+1] = 10000000
frst = [-1]*(n+2)
#print(frst)

ques = input().split()
for i in range(len(ques)):
    ques[i] = int(ques[i])
#print(type(ques[i]))
    
ans = n * 3

for i in range(k):
    
    if frst[ques[i]] == -1 :
            frst[ques[i]] = i    
    #if last[ques[i]] < i :
    last[ques[i]] = i    

    '''try:
        if frst[ques[k]] > k :
            frst[ques[k]] = k    
        if last[ques[k]] < k :
            last[ques[k]] = k    
    except :
        print(("k : {}".format(k)))'''
    '''for x in range(1 , n+1) :
        if last[x] == int(-1) :
            print(x)
            frst[x] = -1
            last[x] = 10000000'''
#print(frst)
#print(last)
cnt = 0
for i in range(1 , n+1):
    if frst[i] != -1 :
        if frst[i] < last[i-1]:
            cnt += 1
        if frst[i] < last[i+1] :
            cnt += 1
            #print("fst : {} < lst : {}").format(frst[i] , last[i+1])
        if frst[i] != -1 :
            cnt += 1
if frst[1] == -1 : cnt+= 1
if frst[n] == -1 : cnt+= 1

ans = ans - cnt 
print(ans)

