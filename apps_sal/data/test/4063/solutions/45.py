n = int(input())
d = sorted(map(int, input().split()))
k1 = d[int(n/2)-1]+1
k2 = d[int(n/2)]
print(k2-k1+1)
