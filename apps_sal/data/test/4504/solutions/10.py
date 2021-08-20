s = str(input())
sl = list(s)
ans = 0
del sl[-1]
for i in range(1, len(sl)):
    if len(sl) % 2 == 0:
        if sl[:len(sl) // 2] == sl[len(sl) // 2:]:
            ans = len(sl)
            break
    del sl[-1]
print(ans)
