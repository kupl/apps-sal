n, m = list(map(int, str.split(input())))
for _ in range(n):

    s = input()
    for color in "CMY":

        if color in s:

            print("#Color")
            return

print("#Black&White")

