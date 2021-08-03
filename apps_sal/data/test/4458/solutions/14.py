
N = int(input())
l = list(map(int, input().split()))

counter = 0
curmin = 1e9
for i in l:
    curmin = min(curmin, i)
    if i == curmin:
        counter += 1
print(counter)
