(integer1, integer2, integer3) = map(int, input().split())
if integer2 == integer3:
    print(integer1)
elif integer1 == integer3:
    print(integer2)
else:
    print(integer3)
