N = int(input())
l = list(map(int, input().split()))
counter = 0
curmin = 1000000000.0
for i in l:
    curmin = min(curmin, i)
    if i == curmin:
        counter += 1
print(counter)
