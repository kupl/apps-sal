_, k = input().split()
k = int(k)
p = sorted(list(int(i) for i in input().split()))
print(sum(p[0:k]))
