def encoded_correcttly(right, message):
    for word in right: 
        # Find the heart
        if '<' in message:
            current_index = message.find('<') + 1
            message = message[current_index:]
        else:
            return False

        # Find the 3
        if '3' in message:
            current_index = message.find('3') + 1
            message = message[current_index:]
        else:
            return False


        # Find the word
        for char in word:
            if char in message:
                current_index = message.find(char) + 1
                message = message[current_index:]
            else:
                return False

    # Find the last heart and 3
    
    # Find the heart
    if '<' in message:
        current_index = message.find('<') + 1
        message = message[current_index:]
    else:
        return False


    # Find the 3
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
    
if (encoded_correcttly(l, message)):
    print("yes")
else:
    print("no")

