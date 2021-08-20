(n, m) = map(int, input().split())
data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))
data1.sort()
for i in data1:
    if i in data2:
        print(i)
        break
else:
    print(min(min(data1), min(data2)) * 10 + max(min(data1), min(data2)))
