n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(10**5):
    if (k-1)*i+1 >= n:
        break

print(i)
