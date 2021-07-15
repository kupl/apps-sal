n = int(input())
arr = list(map(int, input().split()))
fives = 0 
if 5 in arr:
    fives = arr.count(5)
nulls = n - fives
fives -= fives % 9
if nulls == 0 :
    print(-1)
else:
    print(int(str(5) * fives + str(0) * nulls))
