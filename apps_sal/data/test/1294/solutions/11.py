import string

num_inputs = int(input())

for _ in range(num_inputs):
    this_input = input()

    working_letters = []
    for s in string.ascii_lowercase:
        this_input = this_input.replace(s * 2, s.upper())
        if s in this_input:
            working_letters.append(s)
    print("".join(sorted(working_letters)))
