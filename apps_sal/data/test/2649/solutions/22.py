n = int(input())
a = []
j = k = 0


def s(a):
    return a[0] + a[1]


def ss(a):
    return a[0] - a[1]


for i in range(n):
    f = list(map(int, input().split()))
    a.append(f)
aa = min(map(s, a))
b = max(map(s, a))
c = min(map(ss, a))
d = max(map(ss, a))
print(max(abs(d - c), abs(b - aa)))
