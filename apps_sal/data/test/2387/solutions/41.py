def main():
    N = int(input())
    up_lines = []
    down_lines = []
    for i in range(N):
        s = input()
        height = 0
        bottom = 0
        for c in s:
            if c == "(":
                height += 1
            else:
                height -= 1
                bottom = min(bottom, height)
        if height > 0:
            up_lines.append((bottom, height))
        else:
            down_lines.append((bottom-height, -height))
    up_lines.sort(reverse=True, key=lambda line: line[0])
    down_lines.sort(reverse=True, key=lambda line: line[0])
    left = 0
    for bottom, height in up_lines:
        if left + bottom < 0:
            print("No")
            return
        left += height
    right = 0
    for bottom, height in down_lines:
        if right + bottom < 0:
            print("No")
            return
        right += height
    if left == right:
        print("Yes")
    else:
        print("No")


def __starting_point():
    main()

__starting_point()
