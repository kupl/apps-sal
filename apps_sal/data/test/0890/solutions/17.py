import itertools

n, l, r, x = input().split()
n = int(n)
l = int(l)
r = int(r)
x = int(x)
numbers = [int(z) for z in input().split()]
numbers = sorted(numbers)
count = 0;
for z in range(2, len(numbers)+1):
    for subset in itertools.combinations(numbers, z):
        total = sum(subset)
        if total >= l and total <= r and subset[-1]-subset[0] >= x:
            count+=1
print(count)

