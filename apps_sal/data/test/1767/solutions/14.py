n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
aOR = 0
bOR = 0
for i in range(n):
    aOR |= a[i]
    bOR |= b[i]
print(aOR + bOR)
