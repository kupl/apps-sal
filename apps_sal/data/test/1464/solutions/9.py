cs1 = {chr(x) for x in range(ord('a'), ord('z') + 1)}
cs2 = {x + y for x in cs1 for y in cs1}
for i in range(int(input())):
    s = input()
    for i in range(len(s) - 1):
        cs1.discard(s[i:i + 1])
        cs2.discard(s[i:i + 2])
    cs1.discard(s[len(s) - 1:len(s)])
print(min(cs1) if cs1 else min(cs2))
