a = input()
b = input()

mapping = {}

for I in range(len(a)):
    mapping[a[I]] = b[I]

c = input()

answer = ""

for I in c:
    if I.isupper():
        answer += mapping[I.lower()].upper()
    elif I.islower():
        answer += mapping[I]
    else:
        answer += I
print(answer)
