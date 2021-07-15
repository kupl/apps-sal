li=[2,1]
N=int(input())
for i in range(N):
    li.append(li[i]+li[i+1])
print((li[N]))

