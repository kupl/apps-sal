w_list = list(map(int, input().split()))

if w_list.count(5) == 2 and w_list.count(7) == 1:
    print("YES")

else:
    print("NO")
