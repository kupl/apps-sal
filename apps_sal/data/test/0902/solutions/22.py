n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
max1 = max(a)
b = []
done = False
for i in range(n):
    b.append(0)
m = a.index(max1)
if(k > m):
    print(max1)
else:
    curr = 0
    for i in range(1, m):
        if(a[curr] > a[i]):
            # print(b)
            b[curr] += 1
        else:
            curr = i
            b[curr] += 1
        if(max(b) >= k):
            done = True
            print(a[b.index(max(b))])
            break
    if(not done):
        print(max1)
