def generate_acronym(l1: list) -> str:
    answer = ''
    for (i, word) in enumerate(l1):
        answer += word[0].upper()
    return answer


lists = list(map(str, input().split()))
print(generate_acronym(lists))
