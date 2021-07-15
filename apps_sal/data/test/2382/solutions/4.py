def main():
    n = int(input())
    s = list(map(int, input().split(' ')))

    s = sorted(s)[::-1]

    slimes = [s[0]]
    s = s[1:]

    for i in range(n):
        make_slimes = []
        rest_slimes = []
        make_idx = 0
        for j in range(2 ** i):
            for tmp_make_idx in range(make_idx, len(s)):
                if slimes[j] > s[tmp_make_idx]:
                    make_slimes.append(s[tmp_make_idx])
                    break
                else:
                    rest_slimes.append(s[tmp_make_idx])
            make_idx = tmp_make_idx + 1
        rest_slimes += s[make_idx:]
        if len(make_slimes) < 2 ** i:
            print("No")
            return
        slimes += make_slimes
        s = rest_slimes
        slimes = sorted(slimes)[::-1]
        s = sorted(s)[::-1]
    print("Yes")


main()

