N = int(input())
d = [int(i) for i in input().split()]
e = sorted(d)
print(e[int(N / 2)] - e[int(N / 2) - 1])
