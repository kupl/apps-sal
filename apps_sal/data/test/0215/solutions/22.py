def main():
    n = int(input())
    s = input()
    low_chars = set()
    max_power = 0
    for c in s:
        if c.isupper():
            max_power = max(max_power, len(low_chars))
            low_chars = set()
        else:
            low_chars.add(c)
    if len(low_chars) > 0:
        max_power = max(max_power, len(low_chars))
    print(max_power)


main()
