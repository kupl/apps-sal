a, b, c = map(int, input().split())
if sum([a, b, c]) == max(a, b, c) * 2:
    print("Yes")
else:
    print("No")
