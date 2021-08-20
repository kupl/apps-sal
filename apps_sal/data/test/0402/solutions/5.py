(n, k) = list(map(int, input().split()))
a = 0
ind = 0
while a <= 240 - k and ind <= n:
    a += ind * 5 + 5
    ind += 1
a -= ind * 5
print(ind - 1)
