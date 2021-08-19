words = int(input())
message = '<3'
for i in range(words):
    message += input()
    message += '<3'
givenMessage = input()
i = 0
j = 0
while i < len(givenMessage):
    if givenMessage[i] == message[j]:
        j += 1
    if j == len(message):
        break
    i += 1
if j == len(message):
    print('yes')
else:
    print('no')
