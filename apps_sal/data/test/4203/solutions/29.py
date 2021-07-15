import sys

S = input().strip()
if S[0] != "A":
    print("WA")
    return

count = 0
for char in S[2:-1]:
    # print(char)
    if char == "C":
        count += 1
if count != 1:
    print("WA")
    # print("here")
    return

for char in S[1:]:
    if char.isupper() and char != "C":
        print("WA")
        # print("here2")
        return

print("AC")
