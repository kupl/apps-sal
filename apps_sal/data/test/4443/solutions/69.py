C = input()

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

j = 0
for i in alpha:
    if i == C:
        print(alpha[j + 1])
    j += 1
