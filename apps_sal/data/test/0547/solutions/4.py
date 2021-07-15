def count_time(_key):
    i = sorted(variants, key=_key).index(password)
    return i + 1 + i // k * 5


n, k = list(map(int, input().split()))
variants = [input() for x in range(n)]
password = input()
print((*list(map(count_time, [lambda x: (len(x), x != password),
                        lambda x: (len(x), x == password)]))))

