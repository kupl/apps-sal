n, k = map(int, input().split())
print(k*(6*n-1))
for i in range (n):
    print(k*(6*i+1), k * (6*i+3), k*(6*i+4), k * (6*i+5))
