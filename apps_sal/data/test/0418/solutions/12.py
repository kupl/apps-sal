def is_red(x):
    return x >= 2400

n = int(input())
for i in range(n):
    s = input().split()
    a, b = int(s[1]), int(s[2])
    s = s[0]
    if is_red(a) and b > a:
        print("YES")
        return
print("NO")
