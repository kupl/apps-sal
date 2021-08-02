n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
m = -1
num = sum(b)
for i in a:
    if i == m + 1:
        num += c[m - 1]
    m = i
print(num)
