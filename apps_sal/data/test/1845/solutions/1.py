n = int(input())
a = list(map(int,input().split()))
a = sorted(a)

base_sum = sum(a)

smallest = a[0]
min_sum = sum(a)
if n==1:
    print(min_sum)
    return

seen = set()
for x in a[1:]:
    if x in seen:continue
    seen.add(x)
    without = base_sum - a[0] - x
    for div in range(2,x+1):
        if x%div == 0:
            min_sum = min(min_sum,without + smallest*div + x//div)

print (min_sum)
