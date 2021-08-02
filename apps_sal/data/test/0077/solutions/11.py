n = int(input())
lst = [int(x) for x in input().split(" ")]

even = list([x for x in lst if x % 2 == 0])
odd = list([x for x in lst if x % 2 != 0])

even_sum = 0
for i in even:
    if i > 0:
        even_sum += i  # always take all even sums

odd = reversed(sorted(odd))

possible = []
rolling = 0
for i in odd:  # there must be at least one odd number
    rolling += i
    possible.append(even_sum + rolling)

possible = reversed(sorted(possible))
for i in possible:  # print highest sum
    if i % 2 != 0:
        print(i)
        break
