n = int(input())
a = [0]
a.extend(list(map(int, input().split())))
a.append(1001)
longest = 0
i = 0
while i < len(a):
    j = i + 1
    while j < len(a) and a[j - 1] + 1 == a[j]:
        j += 1
    current = j - i - 2
    longest = max(longest, current)
    i = j
print(longest)
