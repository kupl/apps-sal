n = int(input())
lst = list(map(int, input().split()))

sorted_lst = sorted(lst)
mini = sorted_lst[(n//2)-1]
maxi = sorted_lst[(n//2)]
for i in lst:
    if i <= mini:
        print(maxi)
    else:
        print(mini)
