l = list(map(int, input().split()))
k = int(input())
num = max(l)
l.remove(num)
for i in range(k):
    num = num * 2
print(sum(l) + num)
