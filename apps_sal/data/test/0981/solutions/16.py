__author__ = "runekri3"

v = int(input())
digit_costs = [10 ** 7] + list(map(int, input().split()))
temp_list = list(enumerate(digit_costs[:]))
temp_list.sort(key=lambda item: item[1], reverse=True)
temp_list.reverse()
digits_by_price = [digit for digit, cost in temp_list]
cheapest_digit = digits_by_price[0]
extra_costs = [digit_cost - digit_costs[cheapest_digit] for digit_cost in digit_costs]
better_digits = [i for i in range(1, 10) if i > cheapest_digit]
better_digits.sort(reverse=True)

max_len = int(v / digit_costs[cheapest_digit])
if max_len > 0:
    current_number = [str(cheapest_digit)] * max_len
    leftover = v % digit_costs[cheapest_digit]
    for index_being_changed in range(max_len):
        for better_digit in better_digits:
            if extra_costs[better_digit] <= leftover:
                leftover -= extra_costs[better_digit]
                current_number[index_being_changed] = str(better_digit)
                break
        else:  # Not enough paint to change digits
            break
else:
    current_number = "-1"
print("".join(current_number))
