s = input()
alphabets = [0] * 26

for i in s:
    alphabets[ord(i) - ord("a")] += 1

for i in range(26):
    if alphabets[i] == 0:
        print((chr(i + ord("a"))))
        break
else:
    print("None")

