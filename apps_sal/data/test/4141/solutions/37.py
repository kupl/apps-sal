n = int(input())
a = list(map(int, input().split()))
even = []
count = 0

for i in a:
    if i % 2 == 0:
        even.append(i)

for i in even:
    if i % 3 == 0 or i % 5 == 0:
        count += 1

if count == len(even):
    print("APPROVED")
else:
    print("DENIED")
