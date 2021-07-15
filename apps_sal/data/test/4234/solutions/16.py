def main():
    n = int(input())
    s = input()
    stack = []
    ans = 0
    for i in range(n):
        stack.append((s[i], len(stack)))
        if len(stack) > 1:
            if stack[-2][0] == stack[-1][0] and stack[-2][1] % 2 == 0:
                ans += 1
                stack.pop()
    if len(stack) % 2 == 0:
        print(ans)
        for i in range(len(stack)):
            print(stack[i][0], end='')
    else:
        print(ans + 1)
        for i in range(len(stack) - 1):
            print(stack[i][0], end='')



main()

