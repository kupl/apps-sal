n = int(input())

d = [int(i) for i in input().split()]

d.sort()

for i in range(n - 2):
    a = d[i]
    b = d[i + 1]
    c = d[i + 2]
    if a + b > c and a + c > b and b + c > a:
        print("YES")
        break
else:
    print("NO")
