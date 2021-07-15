word = input()

if word[len(word) - 1] == "s":
    print(word + "es")
else:
    print(word + "s")
