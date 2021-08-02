s = input()

print(("".join([c for index, c in enumerate(s) if index % 2 == 0])))
