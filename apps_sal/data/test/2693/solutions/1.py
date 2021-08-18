
import sys


def IOE():
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


def main():
    s, p, k = map(int, sys.stdin.readline().split())
    if k == 1:
        if s == p:
            print(s)
        else:
            print('NO')
    if k == 2:
        for i in range((s // 2) + 1):
            if i * (s - i) == p:
                print(i, s - i)
                break
        else:
            print("NO")
    if k == 3:
        ans = []
        for i in range((s // 3) + 1):
            for j in range((s // 3) + 2):
                if i * j * (s - i - j) == p:
                    ans.append([i, j, s - i - j])

        if len(ans):
            print(*ans[0])
        else:
            print("NO")
    if k == 4:
        ans = []
        for i in range((s // 4) + 1):
            for j in range((s // 4) + 2):
                for k in range((s // 4) + 3):
                    if i * j * k * (s - i - j - k) == p:
                        ans.append([i, j, k, s - i - j - k])
        if len(ans):
            print(*ans[0])
        else:
            print("NO")


def __starting_point():
    main()


__starting_point()
