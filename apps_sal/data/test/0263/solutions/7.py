n=int(input())
m=int(input())
a=[int(input()) for i in range(n)]
max_k= max(a)+m
max_a=max(a)
for ax in a:
    m-=max_a-ax
min_k = max(a)
if m>0:
    min_k += m//n
    if m%n>0:
        min_k+=1
print(min_k, max_k)




