l = list(map(int, input().split()))
la = list(set(l))
if len(la) == 3 or len(la) == 1:
    print("No")
else:
    print("Yes")
