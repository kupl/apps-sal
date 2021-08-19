from collections import Counter
cards_nr = int(input())
number_counter = Counter()
for _ in range(cards_nr):
    curr_number = int(input())
    number_counter[curr_number] += 1
if len(number_counter) != 2:
    print('NO')
else:
    (num1, num2) = list(number_counter)
    if number_counter[num1] != number_counter[num2]:
        print('NO')
    else:
        print('YES')
        print(num1, num2)
