n = int(input())
s = input()
f = bool(n % 2)
rt = []
lt = []
for i in s:
    if (f):
        rt.append(i)
    else:
        lt.append(i)
    f = not f
print("".join(lt[::-1]) + "".join(rt))
