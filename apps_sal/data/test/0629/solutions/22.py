__author__ = 'Om Kumar Sahoo'
n=int(input())
first=[0]+[int(x) for x in input().split()]
second=[int(x) for x in input().split()]+[0]
st=[int(x) for x in input().split()]
firsts=[0]*n
seconds=[0]*n
for i in range(1,n):
    firsts[i]=firsts[i-1]+first[i]
for i in range(n-2,-1,-1):
    seconds[i]=seconds[i+1]+second[i]
time=[0]*n
for i in range(n):
    time[i]=firsts[i]+seconds[i]+st[i]
m1=min(time)
time.remove(m1)
m2=min(time)
print(m1+m2)
