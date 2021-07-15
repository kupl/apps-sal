n = int(input())
s = str(input())
k=n-3
if k>0:
    t=k//2
    for i in range(t,-1,-1):

        s=s.replace('ogo'+'go'*i,'***')
else:
    s=s.replace('ogo','***')
print(s)

