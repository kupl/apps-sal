a=[int(x)for x in input().split()];print(*[sum(a)-2*a[3*(not i%2)]-a[i] for i in[0,1,2,3]])
