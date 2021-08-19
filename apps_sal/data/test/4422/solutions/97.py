def str_replace_to_lower() -> str:
    (len_str, target_index) = map(int, input().split())
    word = input()
    list_of_word = list(word)
    list_of_word[target_index - 1] = list_of_word[target_index - 1].lower()
    return ''.join(list_of_word)


print(str_replace_to_lower())
