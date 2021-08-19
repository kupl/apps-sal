n = int(input())


def read():
    return list(map(int, input().split()))


k = read()
print(min((sum(read()) * 5 + k[i] * 15 for i in range(0, n))))
