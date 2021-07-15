from math import ceil
from math import floor

while True:

    inp = input().split()

    n = int(inp[0])
    a = int(inp[1])
    b = int(inp[2])

    components = input().split('*')

    max_students = 0

    for c in components:

        max_a_b = min( len(c)//2 + len(c)%2, max(a, b) )

        min_a_b = min( len(c)//2, min(a, b) )

        max_students += max_a_b + min_a_b

        if a>=b:

            a -= max_a_b
            b -= min_a_b

        else:

            a -= min_a_b
            b -= max_a_b

    print(max_students)

    break

