n = int(input())
steps = list(map(int, input().split()))
number = 0
single = []
curr = 0
for i in steps:
    if i == 1:
        single.append(curr)
        curr = 1
        number += 1
    else:
        curr += 1
single.append(curr)
print(number)
print(*single[1:])
