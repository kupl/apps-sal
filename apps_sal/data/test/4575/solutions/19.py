n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

tot = 0
for i in range(n):
    tot += int((d-1)/a[i])+1
tot += x
print(tot)
