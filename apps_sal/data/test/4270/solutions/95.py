N = int(input())
Val = list(map(int, input().split()))
Val.sort()
for i in range(N - 1):
    x = Val.pop(0)
    y = Val.pop(0)
    Val.append((x + y) / 2)
    Val.sort()
print(Val[0])
