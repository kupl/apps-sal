def number_rectangle(h):
    l = [0 for i in range(len(h))]
    stack = []
    dp = [0 for i in range(len(h))]
    result = 0
    for i in range(len(h)):
        while len(stack) > 0 and stack[-1] >= h[i]:
            stack.pop()
        if len(stack) == 0:
            dp[i] = i + 1
        else:
            dp[i] = dp[stack[-1]] + (i - stack[-1]) * h[i]
        result += dp[i]
    return result


def main():
    (rows, cols) = list(map(int, input().split()))
    rows += 1
    a = []
    a.append('-' * cols)
    for i in range(1, rows):
        a.append(input())
    h = [[0 for j in range(cols)] for i in range(rows)]
    result = 0
    for i in range(1, rows):
        last_state = (0, 0, 0, 0, 0, 0)
        same_state = 0
        sub = []
        for j in range(0, cols):
            if a[i][j] == a[i - 1][j]:
                h[i][j] = h[i - 1][j] + 1
            else:
                h[i][j] = 1
            i2 = i - h[i][j]
            i3 = i2 - h[i2][j]
            curr_state = (h[i][j], h[i2][j], a[i][j], a[i2][j], a[i3][j])
            if h[i][j] == h[i2][j] and h[i3][j] >= h[i][j]:
                if curr_state == last_state:
                    sub.append(h[i3][j] - h[i][j])
                else:
                    result += number_rectangle(sub)
                    sub.clear()
                    sub.append(h[i3][j] - h[i][j])
            else:
                result += number_rectangle(sub)
                sub.clear()
            last_state = curr_state
        result += number_rectangle(sub)
    result = int(result)
    print(result)


main()
