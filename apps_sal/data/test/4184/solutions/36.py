n=int(input())
w=list(map(int,input().split()))
min=100
for i in range(n-1):
    if min >= abs(sum(w[:i+1])-sum(w[i+1:])):
        min = abs(sum(w[:i+1])-sum(w[i+1:]))
print(min)
