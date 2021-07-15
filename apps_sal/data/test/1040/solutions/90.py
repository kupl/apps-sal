def main():
    N = int(input())
    ans = N
    stack = []
    s = input()
    for c in s:
        if c == "f" or c == "o" or c == "x":
            stack.append(c)
        else:
            stack.clear()
        if c == "x":
            if len(stack) >= 3 and stack[-2] == "o" and stack[-3] == "f":
                ans -= 3
                for i in range(3):
                    stack.pop()
        
    return print(ans) 

def __starting_point():
    main()
__starting_point()
