n = int(input())
l = list(map(int,input().split()))
sorted_list = sorted(l)
left = sorted_list[n//2-1]
right = sorted_list[n//2]
for i in l:
    if i <= left:
        print(right)
    else:
        print(left)
