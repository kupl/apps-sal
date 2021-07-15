n = int(input())
l = list(map(int, input().split()))
odd = []
nodd = []
for i in l:
    if i % 2 == 1:
        odd.append(i)
    else:
        nodd.append(i)
odd.sort()
print(sum(nodd) + sum(odd[len(odd) % 2:]))
