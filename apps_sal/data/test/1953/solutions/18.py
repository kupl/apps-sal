s1 = input()
s2 = [int(i) for i in input().split()]
s2.sort()
k = 0
n = 0
for i in s2:
    if i >= k:
        n += 1
        k += i
print(n)
