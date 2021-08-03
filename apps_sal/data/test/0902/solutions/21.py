# your code goes here
n, k = input().split()
n = int(n)
k = int(k)
a = list(map(int, input().split()))
count = 0
i = 0
j = 1
while True:
    if(k > n):
        print(max(a))
        break
    if(a[i] > a[j]):
        count += 1
        if(count == k):
            print(a[i])
            break
        a.append(a[j])
        a.remove(a[j])
    else:
        a.append(a[i])
        a.remove(a[i])
        count = 1
