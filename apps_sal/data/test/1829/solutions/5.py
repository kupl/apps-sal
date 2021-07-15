x, y = input().split(" ", 1)
x, y = int(x), int(y)
p = {input().strip() for i in range(x)}
q = {input().strip() for i in range(y)}
common = p & q
if len(common) % 2 == 1:
    y -= 1
print("YES" if x > y else "NO")

