from itertools import permutations


mas = [int(i) for i in input().split()]
s = permutations(mas)
for i in s:
    if sum(i[:3]) == sum(i[3:]):
        print("YES")
        return
print("NO")
