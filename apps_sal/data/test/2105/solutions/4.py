(n, m) = map(int, input().split())
nsl = list(map(str, input().split()))
msl = list(map(str, input().split()))
q = int(input())
for rwer in range(q):
    k = int(input())
    print(nsl[(k - 1) % n] + msl[(k - 1) % m])
