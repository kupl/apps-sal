n,m = list(map(int,input().split()))
s = input().split()
t = input().split()
q = int(input())

for _ in range(q):
    a = int(input()) - 1
    print(s[a % n] + t[a % m])

