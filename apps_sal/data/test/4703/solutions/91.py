import itertools
n = input()
l = len(n)
ans = 0
for ope in itertools.product("_+", repeat = l - 1):
    num = n[0]
    for i in range(l - 1):
        if ope[i] == "+":
            num += n[i + 1]
        else:
            ans += int(num)
            num = n[i + 1]
    ans += int(num)
print(ans)
