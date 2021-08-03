n = int(input())
t = list(map(int, input().split()))
t.sort()
count = 0
for i in range(n):
    if(t[i] >= count + 1):
        count += 1
print(count)
