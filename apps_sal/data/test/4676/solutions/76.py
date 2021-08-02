ans = ""
O = input()
E = input()
for o, e in zip(O, E):
    ans += o + e
if len(O) > len(E):
    ans += O[-1]

print(ans)
