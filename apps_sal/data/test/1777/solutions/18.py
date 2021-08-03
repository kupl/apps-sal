from collections import Counter


def cleanup(paren: str) -> str:
    stack = list()

    for char in paren:
        if not stack:
            stack.append(char)
        elif stack[-1] == '(' and char == ')':
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)


def main():
    prob_len = int(input())

    lefts = Counter()
    rights = Counter()
    zeros = 0
    for _ in range(prob_len):
        new_paren = cleanup(input())
        if '(' in new_paren and ')' in new_paren:
            continue
        elif '(' in new_paren:
            lefts.update([len(new_paren)])
        elif ')' in new_paren:
            rights.update([len(new_paren)])
        else:
            zeros += 1

    answer = 0
    answer += zeros // 2
    for paren_num in lefts.keys():
        answer += min(lefts[paren_num], rights[paren_num])

    print(answer)


def __starting_point():
    main()


__starting_point()
