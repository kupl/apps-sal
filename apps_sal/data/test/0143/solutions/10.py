n = int(input())
our = list(map(int, input().split()))
our.sort()
our[0] = 1
for i in range(1, n):
    if our[i] > our[i - 1]:
        our[i] = our[i - 1] + 1
print(our[-1] + 1)
