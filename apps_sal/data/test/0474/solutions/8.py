n = int(input())
s = list(map(int, input().split()))
m = -1
row = 0
mr = 0
for i in s:
    if i == m:
        row += 1
    elif(i > m):
        m = i
        row = 1
        mr = 0
    else:
        row = 0
    mr = max(mr, row)
print(mr)
