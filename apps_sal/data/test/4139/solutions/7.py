import itertools
N = int(input())
count = 0
for i in range(3, len(str(N)) + 1):
    for j in itertools.product('753', repeat=i):
        if int(''.join(j)) <= N and '3' in str(j) and ('5' in str(j)) and ('7' in str(j)):
            count += 1
print(count)
