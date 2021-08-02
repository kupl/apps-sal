t = int(input())
for i in range(t):
    n = int(input())

    lens = sorted(map(int, input().split()))
    cnt = len(list(filter(lambda x: x > 0, lens[:-2])))

    print(min(cnt, lens[-2] - 1))
