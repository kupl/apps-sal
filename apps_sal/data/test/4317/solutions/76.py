(integer1, integer2) = map(int, input().split())
if integer1 + integer2 >= integer1 - integer2:
    if integer1 + integer2 >= integer1 * integer2:
        print(integer1 + integer2)
    else:
        print(integer1 * integer2)
elif integer1 - integer2 >= integer1 * integer2:
    print(integer1 - integer2)
else:
    print(integer1 * integer2)
