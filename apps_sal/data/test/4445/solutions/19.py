n = int(input())
ints = list(map(int, input().split()))
even = []
odd = []
for i in ints:
    if i % 2 == 1:
        odd.append(i)
    else:
        even.append(i)
even.sort()
odd.sort()
if len(even) < len(odd):
    diff = len(odd) - len(even) - 1
    if diff > 0:
        print(sum(odd[0:diff]))
    else:
        print(0)
else:
    diff = len(even) - len(odd) - 1
    if diff > 0:
        print(sum(even[0:diff]))
    else:
        print(0)
