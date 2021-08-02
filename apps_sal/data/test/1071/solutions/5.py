a = sum([int(x) for x in input().split()])
b = sum([int(x) for x in input().split()])
n = int(input())
an, bn = (a + 4) // 5, (b + 9) // 10
if an + bn <= n:
    print("YES")
else:
    print("NO")
