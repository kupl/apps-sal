n = int(input())
lst = [list(map(int,input().split())) for i in range(n)]
lst.sort()
is_happy = False
for i in range(1, n):
    if lst[i][0] > lst[i - 1][0] and lst[i - 1][1] > lst[i][1]:
        is_happy = True
if is_happy:
    print("Happy Alex")
else:
    print("Poor Alex")
