import heapq
n,k=map(int,input().split())
a=[int(o) for o in input().split()]
h=[]
s=set()
j=0
for i in range(n):
    if a[i] not in s:
        heapq.heappush(h,[i,a[i]])
        j+=1
        s.add(a[i])
        if j>k:
            j-=1
            lol=heapq.heappop(h)
            s.remove(lol[1])
st=[]
while h:
    st.append(heapq.heappop(h)[1])
st=st[::-1]
print(len(st))
print(*st)
