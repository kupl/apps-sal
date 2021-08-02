x = input()
max_sections, nuts, divisors, max_nuts = [int(i) for i in x.split()]

divisors_per = max_sections - 1
fit = max_sections * max_nuts

boxes = 1
while 1:
    if divisors_per > divisors:
        sections = divisors + 1
        nuts -= sections * max_nuts
        divisors = 0
    else:
        nuts -= fit
        divisors -= divisors_per

    if nuts <= 0:
        break
    else:
        boxes += 1

print(boxes)
