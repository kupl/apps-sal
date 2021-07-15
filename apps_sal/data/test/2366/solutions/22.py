n = int(input())
a = list(map(int,input().split()))
lst = [0]*(max(a)+1)

for i in a:
    lst[i] += 1

num_lst = [0]*(max(a)+1)
for i in range(1,max(a)+1):
    if not lst[i] in [0,1]:
        num_lst[i] = lst[i]*(lst[i]-1)//2
ans = sum(num_lst)

for i in a:
    if lst[i] in [0,1]:
        print(ans)
    else:
        print(ans-num_lst[i]+((lst[i]-1)*(lst[i]-2)//2))
