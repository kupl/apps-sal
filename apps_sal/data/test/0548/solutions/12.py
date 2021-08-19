n = int(input())
arr = [int(i) for i in input().split()]
tot = 0
odd = 0
even = 0
for i in range(n):
    if arr[i] & 1:
        odd += 1
    else:
        even += 1
    tot += arr[i]
if tot & 1:
    print('First')
elif n == even:
    print('Second')
else:
    print('First')
