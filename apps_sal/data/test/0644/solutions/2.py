l = int(input())
ans = 0
nest = 0
F = []
m = 1
for _ in range(l):
    com = input()
    if com == "add":
        ans += m
        if ans >= 2**32:
            ans = "OVERFLOW!!!"
            break
    elif com == "end":
        m //= F.pop()
    else:
        if m > 2**40:
            a = 1
        else:
            a = int(com.split()[1])
        F.append(a)
        m *= a

print(ans)
