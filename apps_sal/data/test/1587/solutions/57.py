def __starting_point():
    n = int(input())
    s = list(input())

    # 完成品の並びにする
    ss = sorted(s)

    cnt = 0
    # 切り替わりの地点まで＝Wが見つかる部分まで
    if "W" in s:
        sind = ss.index("W")

        # sindまでに含まれるWの数？
        cnt = 0
        for i in range(sind):
            if s[i] == "W":
                cnt += 1

    print(cnt)


__starting_point()
