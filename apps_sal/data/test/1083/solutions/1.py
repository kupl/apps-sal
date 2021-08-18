
n = int(input())

decide = list(range(1, n % 4 + 1))
n_sum = 0
first_group = []
if n % 4 == 1:
    n_sum = 1
if n % 4 == 2:
    n_sum = 1
    first_group.append(2)
if n % 4 == 3:
    n_sum = 0
    first_group.append(3)
k = n
while k > 3:
    first_group.append(k)
    first_group.append(k - 3)
    k -= 4
print(n_sum)
print(len(first_group), *first_group)
