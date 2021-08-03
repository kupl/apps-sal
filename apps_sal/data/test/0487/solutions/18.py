n = int(input())
arr = list(map(int, input().split()))
maxval = max(arr)
sumx = sum(arr)
flag = 0
while((maxval) * n - sumx <= sumx):
    maxval += 1
print(maxval)
