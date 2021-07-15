k,n = map(int,input().split())
an = list(map(int,input().split()))
an.append(k + an[0])
max_length = 0
for i in range(n):
    max_length = max(max_length,an[i+1]-an[i])

print(k-max_length)
