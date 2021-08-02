total = int(input())
initial = int(input())
if initial > total:
    initial = total
a = int(input())
b = int(input())
count = 0
for i in range(initial):
    count += a
for c in range(total - initial):
    count += b

print(count)
