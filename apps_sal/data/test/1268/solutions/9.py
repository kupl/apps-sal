n = int(input())

a = [int(i) for i in input().split(" ")]
b = [int(i) for i in input().split(" ")]
b = sorted(b)

if sum(a) > b[-1] + b[-2]:
    print("NO")
else:
    print("YES")
