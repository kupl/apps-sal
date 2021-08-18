from collections import deque


def f(s1):
    return s1 in "<{[("


s = list(input())

d = deque([])
ans = 0
for i in s:
    if f(i):
        d.append(i)
    else:
        if len(d) == 0:
            print("Impossible")
            return
        elif ord(d[-1]) + 2 == ord(i) or ord(d[-1]) + 1 == ord(i):
            d.pop()
        else:
            d.pop()
            ans += 1
if len(d) > 0:
    print("Impossible")
    return
print(ans)
