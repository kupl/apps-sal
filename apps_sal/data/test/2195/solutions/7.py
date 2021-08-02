LI = lambda: list(map(int, input().split()))
MI = lambda: map(int, input().split())
yes = lambda: print("Yes")
no = lambda: print("No")
I = lambda: list(input())
J = lambda x: "".join(x)
II = lambda: int(input())
SI = lambda: input()
# ---khan17---template
t = II()
for i in range(t):
    x, y = MI()
    a, b = MI()
    if b > 2 * a:
        print((x + y) * a)
    else:
        c = abs(x - y) * a + min(x, y) * b
        print(c)
