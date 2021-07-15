N, K = map(int, input().split())
h = list(map(int, input().split()))

h_l = [int(i) for i in h if i >= K]

print(len(h_l))
