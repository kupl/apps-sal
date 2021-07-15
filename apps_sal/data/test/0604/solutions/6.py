n = int(input())
num = list(map(int, input().split()))
a = []
for i in range(n):
    if num[i]:
        a.append(num[i])
print(len(set(a)))
