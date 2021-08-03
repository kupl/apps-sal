n, k = list(map(int, input().split()))
d = list(map(int, input().split()))
# print(d)
for i in range(n, 10**5):
    count = 0
    for j in range(k):
        u = str(d[j])
        if(str(i).count(u) == 0):
            count += 1
    # print("count:"+str(count))
    if(count == k):
        print(i)
        break
