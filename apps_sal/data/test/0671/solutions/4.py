def read():
    return list(map(int, input().split()))


n = int(input())
a = [i for i in range(1, 1000)]
b = ''.join(map(str, a))
print(b[n - 1])
