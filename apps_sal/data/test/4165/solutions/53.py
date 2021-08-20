n = int(input())
l = list(map(int, input().split()))
sum = 0
for i in range(n):
    sum += l[i]
print('Yes' if max(l) * 2 < sum else 'No')
