n = int(input())
for i in range(n):
    d = input()
    u = sorted(d)
    if u == u[::-1]:
        print(-1)
    else:
        print("".join(u))
