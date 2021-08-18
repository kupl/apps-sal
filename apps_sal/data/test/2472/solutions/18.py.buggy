n = int(input())
x = [list(map(int, input().split())) for i in range(n)]
y = []
y = sorted(x, key=lambda x: x[1])
a = 0
for i in y:
    a += i[0]
    if a > i[1]:
        print("No")
        return
print("Yes")
