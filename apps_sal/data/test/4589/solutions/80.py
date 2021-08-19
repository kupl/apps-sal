import sys

input = sys.stdin.readline


def main():
    ans = []
    b = "#"
    h, w = map(int, input().split())
    s = [input().rstrip('\n') for _ in range(h)]
    for y in range(h):
        ans.append([])
        for x in range(w):
            if s[y][x] == b:
                ans[y].append(b)
            else:
                ans[y].append(0)
    for y in range(h):
        for x in range(w):
            if s[y][x] == b:
                if y > 0 and x > 0 and ans[y - 1][x - 1] != b:
                    ans[y - 1][x - 1] += 1
                if y > 0 and ans[y - 1][x] != b:
                    ans[y - 1][x] += 1
                if y > 0 and x < w - 1 and ans[y - 1][x + 1] != b:
                    ans[y - 1][x + 1] += 1
                if x > 0 and ans[y][x - 1] != b:
                    ans[y][x - 1] += 1
                if x < w - 1 and ans[y][x + 1] != b:
                    ans[y][x + 1] += 1
                if y < h - 1 and x > 0 and ans[y + 1][x - 1] != b:
                    ans[y + 1][x - 1] += 1
                if y < h - 1 and ans[y + 1][x] != b:
                    ans[y + 1][x] += 1
                if y < h - 1 and x < w - 1 and ans[y + 1][x + 1] != b:
                    ans[y + 1][x + 1] += 1
    for y in range(h):
        for x in range(w):
            if ans[y][x] == 0 and s[y][x] == b:
                ans[y][x] = "#"
            else:
                ans[y][x] = str(ans[y][x])
        print(''.join(ans[y]))


def __starting_point():
    main()


__starting_point()
