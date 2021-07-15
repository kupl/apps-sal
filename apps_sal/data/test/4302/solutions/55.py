A,B = map(int,input().split())
count=0
for _ in range(2):
       if A>=B:count+=A;A-=1
       else :count+=B;B-=1
print(count)
