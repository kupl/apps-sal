a = list(map(int, input().split()))
if max(a)*2 == sum(a):
    print("Yes")
else:
    print("No")
