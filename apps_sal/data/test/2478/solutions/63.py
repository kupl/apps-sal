def main():
    N = int(input())
    S = input()
    brackets = [0, 0]
    for i in range(len(S)):
        if S[i] == ')':
            if brackets[0] > 0:
                brackets[0] -= 1
            else:
                brackets[1] += 1
        elif S[i] == '(':
            brackets[0] += 1
    print(brackets[1] * '(' + S + brackets[0] * ')')


main()
