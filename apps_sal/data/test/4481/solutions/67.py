def sovle():
    N = int(input())
    d = {}
    max = []
    max_count = 0
    for i in range(N):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
        if max_count < d[s]:
            max = [s]
            max_count = d[s]
        elif max_count == d[s]:
            max.append(s)
    max.sort()
    for i in max:
        print(i)


sovle()
