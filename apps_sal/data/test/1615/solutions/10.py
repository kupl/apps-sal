l = list(map(int, input().split()))
n, k = l[0], l[1]
i = 0
sum = 0
while(i < n):
    l = list(map(int, input().split()))
    l = list(range(l[0], l[1] + 1))
    sum += len(l)
    i += 1
if(sum % k == 0):
    print(0)
else:
    print(((sum // k) + 1) * k - sum)
