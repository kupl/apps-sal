a,b = list(map(int,input().split()))
count = 0
for i in range(a,b+1):
    s = str(i)
    if s == s[::-1]:
        count += 1
print(count)

