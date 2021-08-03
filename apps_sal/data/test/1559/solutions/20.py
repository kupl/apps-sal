def revive(l):
    res = pow(10, l - 1)
    return str(res)


l = int(input())
s = input()
val = 0
if len(s) % l == 0:
    ans = s[:l]
    if ans * (len(s) // l) > s:
        print(ans * (len(s) // l))
        return
    elif ans == "9" * l:
        ans = revive(l)
        val = l
    else:
        ans = str(int(ans) + 1)
else:
    ans = revive(l)
print(ans * ((len(s) + l - 1 + val) // l))
