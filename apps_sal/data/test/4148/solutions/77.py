N = int(input())
print("".join(map(lambda x: chr((ord(x) - 65 + N) % 26 + 65), input())))
