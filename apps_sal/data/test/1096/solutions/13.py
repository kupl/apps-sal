position = input()

result = 8

if position in {'a1', 'a8', 'h1', 'h8'}:
    result = 3
elif position[0] in {'a', 'h'} or position[1] in {'1', '8'}:
    result = 5
print(result)

