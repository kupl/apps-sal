N = int(input())
S = input()

new_s = []
for c in S:
    new_s.append(chr((ord(c) - ord("A") + N) % 26 + ord("A")))

print("".join(new_s))
