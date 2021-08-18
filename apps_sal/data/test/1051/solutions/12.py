

n = int(input())
l = list(map(int, input().split()))
if max(l) > 25:
    print(max(l) - 25)
else:
    print(0)
