n, m = list(map(int, input().split()))
s = list(input().split())
t = list(input().split())
q = int(input())
for _ in range(q):
    e = int(input()) - 1
    print(s[e % n] + t[e % m])
