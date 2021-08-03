def input_ints():
    return [int(x) for x in input().split()]


input()
xs = input_ints()

print(2 + (xs[2] ^ min(xs)))
