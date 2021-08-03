n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
y.sort()
if sum(x) <= y[-1] + y[-2]:
    print("YES")
else:
    print("NO")
