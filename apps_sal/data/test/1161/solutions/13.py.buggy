s = input()
open = "({<["
close = ")}>]"
clopen = {']': '[', '}': '{', '>': '<', ')': '('}
ir2 = 0
ir = 0
if len(s) % 2 == 1:
    print("Impossible")
    return
else:
    l = []
    for i in range(len(s)):
        if s[i] in open:
            ir += 1
            l.append(s[i])
        else:
            ir -= 1
            if ir == -1:
                print("Impossible")
                return
            p = l.pop()
            if clopen[s[i]] != p:
                ir2 += 1
if ir != 0:
    print("Impossible")
    return
else:
    print(ir2)
