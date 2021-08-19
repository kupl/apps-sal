n = int(input())
a = list(map(int, input().strip().split()))

first_appearance = dict()
last_appearance = dict()
for idx, elem in enumerate(a):
    last_appearance[elem] = idx
    if elem not in first_appearance:
        first_appearance[elem] = idx


# print(first_appearance)
# print(last_appearance)

last_last = -1
num_choice_elem = 0
for idx, elem in enumerate(a):
    if idx > 0:
        if first_appearance[elem] == idx and last_last <= idx:
            num_choice_elem += 1
            # print(idx, elem)

    temp = last_appearance[elem]
    if temp >= idx and last_last <= temp:
        last_last = temp


final = 1
for _ in range(num_choice_elem):
    final *= 2
    final = final % 998244353

print(final)
