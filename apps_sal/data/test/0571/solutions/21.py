def main():
    n = int(input())
    s = list(input())
    temp_count = 0
    for c in s:
        if c == '(':
            temp_count += 1
    stack = []
    for i in range(n):
        if i == n - 1 and (len(stack) != 1 or s[i] == '('):
            print(':(')
            return
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if not stack:
                print(':(')
                return
            stack.pop()
        elif i != n - 1 and temp_count < n // 2:
            s[i] = '('
            stack.append('(')
            temp_count += 1
        else:
            s[i] = ')'
            stack.pop()
        if i != n - 1 and (not stack):
            print(':(')
            return
    print(''.join(s))


def __starting_point():
    main()


__starting_point()
