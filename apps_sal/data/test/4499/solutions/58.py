def generate_acronym(l1: list) -> str:
    answer = ""
    for word in l1:
        # answer.append(word[0].upper())
        answer += word[0].upper()

    return answer


lists = list(map(str, input().split()))
print((generate_acronym(lists)))
