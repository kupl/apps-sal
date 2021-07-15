n, k = map(int, input().split( ))
a = n%k
b = (-n)%k
print(min(a, b))
