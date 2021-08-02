N = int(input())
A = list(map(int, input().split()))

even = []
approved = 0

for i in A:
    if i % 2 == 0:
        even.append(i)

for x in even:
    if x % 3 == 0 or x % 5 == 0:
        approved += 1

if approved == len(even):
    print("APPROVED")
else:
    print("DENIED")
