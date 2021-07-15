n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = [x-y for x,y in zip(a,b)]
l.sort()
z = l.count(0)
p = sum(1 for x in l if x > 0)
m = n - z - p
idx = n
cnt = p*(p-1)//2 + z*p
for i in range(m):
    while l[idx-1] + l[i] > 0: idx -= 1
    cnt += n - idx
print(cnt)
