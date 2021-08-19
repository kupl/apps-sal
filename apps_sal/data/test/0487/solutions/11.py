n = int(input())
a = list(map(int, input().split()))
s = sum(a)
k = max(a)
while True:
    if n * k - s > s:
        print(k)
        break
    k += 1
