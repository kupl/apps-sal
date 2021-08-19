(integer1, integer2, term) = map(int, input().split())
term_value = max(integer1, integer2)
largest_term = 0
while term_value <= 100:
    if integer1 % term_value == 0 and integer2 % term_value == 0:
        largest_term += 1
    if term == largest_term:
        break
    term_value -= 1
print(term_value)
