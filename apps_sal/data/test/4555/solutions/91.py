a,b,k=map(int, input().split())
an=[]
for i in range(a,min(a+k,b+1)):
    an.append(i)
for i in range(max(b-k+1,a),b+1):
    an.append(i)
an=sorted(list(set(an)))
for i in an:
    print(i)
