n = int(input())
l = list(map(int, input().split()))
k = 0
while l[k] == l[-1]:
    k += 1
m = len(l) - 1 - k
k = len(l) - 1
while l[k] == l[0]:
    k -= 1
m = max(m, k)
print(m)
