n, s = list(map(int, input().split()))
count = 0
for i in range(n):
    count += (s // (n - i))
    s -= (s // (n - i)) * (n - i)
print(count)
