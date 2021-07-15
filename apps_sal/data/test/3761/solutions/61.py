import sys
readline = sys.stdin.readline

def main():
    s = readline()
    X, Y = list(map(int, readline().split()))

    data = []
    step, temp_T = 0, 0
    for c in s:
        if c == 'F':
            step += 1
        else:
            if step == 0:
                temp_T += 1
            else:
                data.append([step, temp_T])
                step = 0
                temp_T = 1

    for i in range(1, len(data)):
        data[i][1] += data[i - 1][1]

    right, horizontal, vertical = 0, [], []
    for s, t in data:
        if t == 0:
            right += s
        elif t & 1:
            vertical.append(s)
        else:
            horizontal.append(s)

    dp_h, dp_v = {}, {}
    dp_h[right] = 1; dp_v[0] = 1
    for dx in horizontal:
        dp_h_temp = {}
        for x in dp_h:
            if x + dx in dp_h_temp:
                dp_h_temp[x + dx] += dp_h[x]
            else:
                dp_h_temp[x + dx] = dp_h[x]
            if x - dx in dp_h_temp:
                dp_h_temp[x - dx] += dp_h[x]
            else:
                dp_h_temp[x - dx] = dp_h[x]
        dp_h = dp_h_temp.copy()

    for dy in vertical:
        dp_v_temp = {}
        for y in dp_v:
            if y + dy in dp_v_temp:
                dp_v_temp[y + dy] += dp_v[y]
            else:
                dp_v_temp[y + dy] = dp_v[y]
            if y - dy in dp_v_temp:
                dp_v_temp[y - dy] += dp_v[y]
            else:
                dp_v_temp[y - dy] = dp_v[y]
        dp_v = dp_v_temp.copy()

    print(('Yes' if X in dp_h and Y in dp_v else 'No'))

def __starting_point():
    main()

__starting_point()
