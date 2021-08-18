n = int(input())
s = input()

result = ""

for c in s:
    result += chr(ord("A") + (ord(c) - ord("A") + n) % 26)

print(result)
