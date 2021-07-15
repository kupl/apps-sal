from collections import Counter


number_of_words = int(input())
input_string = input()
words_dict = Counter(input_string)
if len(words_dict) < number_of_words:
    print('NO')
else:
    print('YES')
    if number_of_words == 1:
        print(input_string)
    else:
        using_letters = []
        for i in range(0, number_of_words - 1):
            output_string = ''
            current_letter = input_string[0]
            using_letters += current_letter
            while True:
                if input_string[0] in using_letters:
                    output_string += input_string[0]
                    input_string = input_string[1:]
                else:
                    break
            print(output_string)
        print(input_string)
