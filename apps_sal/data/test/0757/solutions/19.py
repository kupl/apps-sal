n, m, k = list(map(int,input().split()))
line = [int(x) for x in input().split()]
line.sort(reverse = True)
count = 0
if k >=m:
    print(count)
    return
for i in range(n):
    k += line[i]-1
    count += 1
    if k >= m:
        print(count)
        return
print(-1)

