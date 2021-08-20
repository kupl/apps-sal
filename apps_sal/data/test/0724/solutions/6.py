f = input()
(n, d) = f.split()
(n, d) = (int(n), int(d))
f = input()
a = f.split()
a = [int(k) for k in a]
ans = 0
count = 0
for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] <= a[j] <= a[i] + d:
            count += 1
    if count > ans:
        ans = count
print(len(a) - ans)
