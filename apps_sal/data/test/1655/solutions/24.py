n = int(input())
a = [int(i) for i in input().split()]
count = 0
least = n
i = n
while i > 0:
    i -= 1
    if i < least:
        count += 1
    least = min(i - a[i], least)
print(count)
