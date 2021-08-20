n = int(input())
x = [bin(int(i)).count('1') for i in input().split()]
s = 0
for i in range(max(x) + 1):
    s = s + x.count(i) * (x.count(i) - 1)
print(int(s / 2))
