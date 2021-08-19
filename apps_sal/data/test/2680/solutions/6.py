# your code goes here
n, b = list(map(int, input().strip().split()))
lx = list(map(int, input().strip().split()))
ly = list(map(int, input().strip().split()))
x = 0
for i in range(0, b):
    x += min(n - lx[i], lx[i] - 1)
    x += min(n - ly[i], ly[i] - 1)
print(x)
