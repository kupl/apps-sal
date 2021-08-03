input()
s = input()

print("".join(map(str, list(map(len, s.split("0"))))))
