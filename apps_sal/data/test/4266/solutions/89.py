def my_input():
    return list(map(int, input().split()))


(k, x) = my_input()
ans = [x + i for i in range(-(k - 1), k)]
print(*ans, sep=' ')
