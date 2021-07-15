n = int(input())
lst = [int(x) for x in input().split()]
for i in range(len(lst)):
    if lst[i]%2==0:
        lst[i]-=1
lst = [str(x) for x in lst]
print(' '.join(lst))

