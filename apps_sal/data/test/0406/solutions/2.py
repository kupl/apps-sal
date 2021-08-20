def __starting_point():
    input()
    data = sorted(map(int, input().split()), key=lambda x: -x)
    if len(data) < 4:
        print(0)
        return
    total = 0
    i = 0
    while i < len(data) - 3:
        if abs(data[i] - data[i + 1]) > 1:
            i += 1
            continue
        success = False
        for j in range(i + 2, len(data) - 1):
            if abs(data[j] - data[j + 1]) > 1:
                continue
            success = True
            total += min(data[i], data[i + 1]) * min(data[j], data[j + 1])
            i = j + 2
            break
        if not success:
            i += 1
    print(total)


__starting_point()
