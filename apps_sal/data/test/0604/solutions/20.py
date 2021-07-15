n = int(input())
s = list(map(int, input().split()))
s = set(s)
count = 0
for x in s:
    if x!=0:
        count+=1

print(count)
