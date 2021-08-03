n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    s = input()
    t = 0
    for elem in s:
        if elem in "aeiouy":
            t += 1
    if t != a[i]:
        print("NO")
        return
print("YES")
