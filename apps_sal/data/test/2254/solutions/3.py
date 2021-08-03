
n = int(input())

a = list(map(int, input().split()))


for i in range(n):
    x = bin(a[i])
    a[i] = x.count('1')


even = 0
odd = 0
cnt = 0
# print(a)
sofar = 0
for i in range(n):
    sofar += a[i]
    if(sofar % 2):
        odd += 1
    else:
        even += 1
even += 1
# print(even,odd)
sofar = 0
for i in range(n):
    if(sofar % 2):
        odd -= 1
        cnt += odd
    else:
        even -= 1
        cnt += even
    sofar += a[i]

# print(cnt)
for i in range(n):
    sum1 = 0
    max1 = a[i]
    for j in range(i, min(i + 100, n)):
        sum1 += a[j]
        max1 = max(max1, a[j])
        if(sum1 % 2 == 0 and sum1 < 2 * max1):
            cnt -= 1
print(cnt)
