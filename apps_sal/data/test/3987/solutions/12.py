def solve(lst):
    a = b = c = d = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            a += 1
            c = max(b, c) + 1
        else:
            b = max(a, b) + 1
            d = max(c, d) + 1
    return max(a, b, c, d)


n = input()
lst = list(map(int, input().split()))
print(solve(lst))
