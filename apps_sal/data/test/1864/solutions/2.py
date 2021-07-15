n = int(input())
s = [int(i) for i in input().split()]
if min(s) > 1:
    print(1)
else:
    print(-1)

