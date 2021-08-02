T = int(input())
for t in range(T):
    n, k = list(map(int, input().split()))
    tables = input()

    next_ones = [-1 for i in range(n)]
    last_one = -1
    for i in range(n - 1, -1, -1):
        # print(i)
        if tables[i] == "1":
            next_ones[i] = i
            last_one = i
        else:
            next_ones[i] = last_one

    prev_one = -1
    res = 0
    for i in range(n):
        if tables[i] == "1":
            prev_one = i
        else:
            if prev_one == -1 or i - prev_one > k:
                if next_ones[i] == -1 or next_ones[i] - i > k:
                    res += 1
                    prev_one = i

    print(res)
