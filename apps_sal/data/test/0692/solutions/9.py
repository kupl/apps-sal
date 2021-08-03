N = int(input())
M = list(map(int, input().split()))
R = list(map(int, input().split()))


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


lcm = 1
for i in range(N):
    lcm = lcm * M[i] / gcd(lcm, M[i])
rec = set()
for i in range(N):
    j = R[i]
    while j < lcm:
        rec.add(j)
        j += M[i]
print(len(rec) / lcm)
