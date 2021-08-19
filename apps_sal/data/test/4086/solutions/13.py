# your code goes here
n = int(input())
l = list(map(int, input().split()))
rdup = []
l = l[::-1]
for i in l:
    if i not in rdup:
        rdup.append(i)
rdup = rdup[::-1]
print(len(rdup))
for i in rdup:
    print(i, end=' ')
