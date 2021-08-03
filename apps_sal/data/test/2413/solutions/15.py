
t = int(input())
for i in range(t):
    n = int(input())
    s = input()

    l = s.find("1")
    r = n - 1 - s.rfind("1")

    if l < 0:
        print(n)
    else:
        mn = min(l, r)
        print((n - mn) * 2)
