n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
h = [abs((t - i * 0.006) - a) for i in h]
print(h.index(min(h)) + 1)
