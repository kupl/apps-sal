r, c = list(map(int, input().split()))

for _ in range(r - 1):
    input()

bottom = input()

sections = 0

looking_for_new_section = True


for brick in bottom:
    if looking_for_new_section:
        if brick == 'B':
            looking_for_new_section = False
            sections += 1
    else:
        if brick == '.':
            looking_for_new_section = True

print(sections)
