n, m = list(map(int, input().split()))
s = input().split()
t = input().split()

for _ in range(int(input())):
    y = int(input()) - 1
    print(s[y % n] + t[y % m])
