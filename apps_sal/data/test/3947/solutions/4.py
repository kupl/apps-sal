def maxScore(list):
    score = 0
    stack = []
    stack.append(list[0])
    for i in range(1, len(list)):
        while len(stack) > 1 and stack[-1] <= min(list[i], stack[-2]):
            score = score + min(list[i], stack[-2])
            stack.pop()
        stack.append(list[i])
    for i in range(1, len(stack) - 1):
        score = score + min(stack[i - 1], stack[i + 1])
    return score


input()
l = [int(x) for x in input().split()]
print(maxScore(l))
