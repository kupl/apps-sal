n, k, p = (int(x) for x in input().split())
a = sorted([int(x) for x in input().split()])
b = sorted([int(x) for x in input().split()])

time = min([max([abs(a[j] - b[i + j]) + abs(b[i + j] - p) for j in range(n)]) for i in range(k-n+1)])

print(time)  
