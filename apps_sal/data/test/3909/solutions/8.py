i = int(input())
k = 1
while i % k == 0:
    k = k * 3
print(i // k + 1)
