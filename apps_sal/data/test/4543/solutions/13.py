a, b = map(int, input().split())
m = b + a * 10 ** len(str(b))
find = False;
for i in range(m):
    if m == i ** 2:
        find = True;
if find:
    print("Yes")
else:
    print("No")
