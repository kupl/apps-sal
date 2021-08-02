def is_leap(n):
    return n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)


curr = int(input())
leapness = is_leap(curr)
first = 0
while True:
    if is_leap(curr):
        first += 1
    first += 1
    first %= 7
    curr += 1
    if first == 0 and leapness == is_leap(curr):
        break
print(curr)
