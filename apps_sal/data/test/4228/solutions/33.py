n, l = list(map(int, input().split()))
azi = [l+i-1 for i in range(1, n+1)]
diff = [0]*n
for i in range(n):
    diff[i] = abs(azi[i])

if sum(azi) < 0:
    print((sum(azi) + abs(min(diff))))
else:  
    print((sum(azi) - min(diff)))


