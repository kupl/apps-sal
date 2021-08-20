print((lambda n: (lambda data, k: sum((min(data[i::k].count(1), data[i::k].count(2)) for i in range(k))))(list(map(int, input().split())), int(n[1])))(input().split()))
