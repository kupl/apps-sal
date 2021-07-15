n = int(input())

ans = 0


def gen_pat(cur):
    nonlocal ans

    if int(cur) > n:
        return

    if len(set(cur)) == 4:  # 0 7 5 3 が含まれる。
        ans += 1

    gen_pat(cur + "3")
    gen_pat(cur + "5")
    gen_pat(cur + "7")


gen_pat("0")
print(ans)

