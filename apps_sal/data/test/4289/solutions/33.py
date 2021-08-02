n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
kaiteki = [abs(t - i * 0.006 - a) for i in h]
print(kaiteki.index(min(kaiteki)) + 1)
