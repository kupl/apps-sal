def coun(pref):
    now = 0
    for i in range(n):
        pos = pref[i]
        if pos == 'l':
            if i < n - 1 and sum(check[(i + 1):]) > 0:
                now += 1
                if "1" in mat[i]:
                    if pref[i + 1] == "r":
                        now += (m + 1)
                    else:
                        now += (2 * mat[i].rfind("1"))
                else:
                    if pref[i + 1] == 'r':
                        now += (m + 1)
            else:
                if "1" in mat[i]:
                    now += mat[i].rfind("1")
        else:
            if i < n - 1 and sum(check[(i + 1):]) > 0:
                now += 1
                if "1" in mat[i]:
                    if pref[i + 1] == "l":
                        now += (m + 1)
                    else:
                        now += (2 * (m + 1 - mat[i].find("1")))
                else:
                    if pref[i + 1] == 'l':
                        now += (m + 1)
            else:
                if "1" in mat[i]:
                    now += (m + 1 - mat[i].find("1"))
    return now


def gen(pref):
    nonlocal ans
    if len(pref) == n:
        ans = min(ans, coun(pref))
        return
    gen(pref + "l")
    gen(pref + "r")


n, m = map(int, input().split())
mat = [0] * n
for i in range(n):
    mat[i] = input()
mat.reverse()
check = [0] * n
for i in range(n):
    check[i] = mat[i].count("1")
ans = 1000000000
gen("l")
print(ans)
