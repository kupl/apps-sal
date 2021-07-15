n = int(input())
total = 0
for i in range(n):
    l, r = map(int,input().split())
    total += r - l + 1
print(total)
