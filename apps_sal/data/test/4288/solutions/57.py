arr = list(map(int , input().split()))
if len(set(arr)) == 2:
    print("Yes")
else:
    print("No")
