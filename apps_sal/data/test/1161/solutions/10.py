stack = []

def main():
    s = str(input())
    open = list("<{[(")
    close = list(">}])")

    answer = 0

    for e in s:
        if len(stack) == 0:
            if e in open:
                stack.append(e)
            else:
                print("Impossible")
                return
        else:
            top = len(stack) - 1
            if e in open:
                if stack[top] in close:
                    if open.index(e) != close.index(stack[top]):
                        answer += 1

                    stack.pop(top)
                else:
                    stack.append(e)
            else:
                if stack[top] in close:
                    stack.append(e)
                else:
                    if close.index(e) != open.index(stack[top]):
                        answer += 1

                    stack.pop(top)

    if len(stack) != 0:
        print("Impossible")
    else:
        print(answer)

def __starting_point():
    main()
__starting_point()
