def Checker(hint, card):
    for a in card:
        for b in card:
            if a == b:
                continue
            elif a[0] == b[0]:
                if a[1] not in hint and b[1] not in hint:
                    return False
            elif a[1] == b[1]:
                if a[0] not in hint and b[0] not in hint:
                    return False
            elif a[0] not in hint and a[1] not in hint and b[0] not in hint and b[1] not in hint:
                return False
    return True


user_input = int(input())
user_input = input()
Card = user_input.split(' ')
possible_chars = "RGBYW12345"

final_answer = 10

card_set = set(Card)
if len(card_set) == 1:
    print("0")

else:

    for i in range(1024):
        hint = ""
        counter = 0
        for j in range(9, -1, -1):
            if (i - (2**j)) > 0:
                hint += possible_chars[j]
                i -= 2**j
                counter += 1

        if Checker(hint, card_set):
            final_answer = min(final_answer, counter)

    print(final_answer)
