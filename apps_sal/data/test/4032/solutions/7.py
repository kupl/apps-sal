n, k = input().split()
n = int(n)
k = int(k)
a = list(map(int, input().split()))
i = 0
count = 0
while(i < n):
    if(a[i] <= k):
        count += 1
        i += 1
    else:
        break
j = n - 1
while(j > i):
    if(a[j] <= k):
        count += 1
        j -= 1
    else:
        break
print(count)
