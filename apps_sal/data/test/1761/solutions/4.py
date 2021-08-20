def encoded_correcttly(right, message):
    for word in right:
        if '<' in message:
            current_index = message.find('<') + 1
            message = message[current_index:]
        else:
            return False
        if '3' in message:
            current_index = message.find('3') + 1
            message = message[current_index:]
        else:
            return False
        for char in word:
            if char in message:
                current_index = message.find(char) + 1
                message = message[current_index:]
            else:
                return False
    if '<' in message:
        current_index = message.find('<') + 1
        message = message[current_index:]
    else:
        return False
    if '3' in message:
        current_index = message.find('3') + 1
        message = message[current_index:]
    else:
        return False
    return True


n = int(input())
l = []
for i in range(n):
    l.append(input())
message = input()
if encoded_correcttly(l, message):
    print('yes')
else:
    print('no')
