n = int(input())
a = list(map(int, input().split()))

d=0
a = [0] + a + [0]
for j in range(len(a)-1):
    d += abs(a[j]-a[j+1])

for i in range(1, len(a)-1):
    if a[i-1] <= a[i] <= a[i+1] or a[i-1] >= a[i] >= a[i+1]:
        print(d)
    else:
        print(d - abs(a[i-1]-a[i]) - abs(a[i+1]-a[i]) + abs(a[i-1]-a[i+1]))
