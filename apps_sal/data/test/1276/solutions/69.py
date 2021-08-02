
def __starting_point():

    n = int(input())
    s = list(input())

    # それぞれの組み合わせ数を求める
    R = s.count("R")
    G = s.count("G")
    B = s.count("B")

    sm = R * G * B
    # print("組み合わせ数="+str(sm))

    # cond2の条件から
    # j-i = k-jの時のkを求める
    # k = 2j - i なので
    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i
            if k < n:
                # print(s[i],s[j],s[k])
                # 等間隔の場合はsmから-1する
                if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                    sm -= 1
    print(sm)


__starting_point()
