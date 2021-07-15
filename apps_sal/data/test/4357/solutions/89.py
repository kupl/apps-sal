a = list(map(int,input().split()))
sort_a = sorted(a,reverse=True)
tmp = int(str(sort_a[0])+str(sort_a[1]))+sort_a[2]
print(tmp)
