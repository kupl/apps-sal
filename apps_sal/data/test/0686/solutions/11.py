

for _ in range(int(input())):
    x, y = map(int, input().split())

    diff = x - y

    if(diff == 1):
        print("NO")
    else:
        print("YES")
