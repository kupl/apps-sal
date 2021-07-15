n = int(input())
colors = list(map(str, input().split()))

if "Y" in colors:
    print("Four")
else:
    print("Three")
