# 桁DPぽいけどただの再帰でいい
n = input()


def rec(i):
    if int(i) > int(n):
        return 0
    ret = 0
    if "3" in i and "5" in i and "7" in i:
        ret += 1
    for j in ["3", "5", "7"]:
        ret += rec(i + j)
    return ret


ans = 0
for i in ["3", "5", "7"]:
    ans += rec(i)
print(ans)
