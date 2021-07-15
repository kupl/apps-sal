n = int(input())

phrase = "I hate "

for i in range(n-1):
    if i % 2 == 0:
        phrase += "that I love "
    else:
        phrase += "that I hate "

print(phrase + "it")

