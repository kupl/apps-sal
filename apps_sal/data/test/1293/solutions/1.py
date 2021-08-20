def read():
    return map(int, input().split())


n = int(input())
a = [0] + list(read())
ans = sum((abs(a[i] - a[i - 1]) for i in range(1, n + 1)))
print(ans)
