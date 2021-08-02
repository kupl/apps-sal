class Solution:
    # https://www.youtube.com/watch?v=y2kFBqj_J08&list=PLLuMmzMTgVK45AiaeeEGGc6xqM6jrlXL4&index=1
    def parseBoolExpr1(self, expression: str) -> bool:
        def helper(queue):
            res = True
            while queue:
                c = queue.pop()
                print(('c = {0}'.format(c)))
                if c in {'t', 'f'}:
                    return True if c == 't' else False
                if c == '!':
                    # remove '('
                    queue.pop()
                    # print('!, queue = {0}'.format(queue))
                    res = not helper(queue)
                    # remove ')'
                    queue.pop()
                    return res
                # elif c in {'&', '|'}:
                    # for &, True & exp1 & exp2, for |, False | exp1 | exp2
                isAnd = True if c == '&' else False
                res = isAnd
                # remove '('
                queue.pop()
                while True:
                    if isAnd:
                        res &= helper(queue)
                    else:
                        res |= helper(queue)
                    # ch can be ')' or ,  e.g \"|(&(t,f,t),!(t))\"
                    print(('isAnd = {0}, queue = {1}, res = {2}'.format(isAnd, queue, res)))
                    ch = queue.pop()
                    print(('after pop char, char = {0}, queue = {1}'.format(ch, queue)))
                    if ch == ')':
                        break
            return res

        queue = collections.deque([])
        for c in expression:
            queue.appendleft(c)
        return helper(queue)

    # slow, time: O(n^2)

    def parseBoolExpr(self, expression: str) -> bool:
        # j is inclusive
        def helper(exp, i, j):
            if i == j:
                return exp[i] == 't'
            op = exp[i]
            res = op == '&'
            # k starts from '('
            k, count, prev = i + 1, 0, i + 2
            # print('i = {0}, j = {1}'.format(i, j))
            while k <= j:
                c = exp[k]
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if (count == 1 and c == ',') or not count:
                    # print('k = {0}, c = {1}, count = {2}, i1 = {3}, j1 = {4}'.format(k, c, count, i + 2, k - 1))
                    val = helper(exp, prev, k - 1)
                    prev = k + 1
                    if op == '!':
                        res = not val
                    elif op == '&':
                        res &= val
                    elif op == '|':
                        res |= val
                k += 1
            # print('i = {0}, j = {1}, res = {2}'.format(i, j, res))
            return res

        return helper(expression, 0, len(expression) - 1)

        # if len(expression) == 1:
        #     return expression == 't'
        # if expression[0] == '!':
        #     return not self.parseBoolExpr(expression[2:-1])
        # op, stack, i = expression[0], [], 2
        # while i < len(expression) - 1:
        #     if expression[i] == 't' or expression[i] == 'f':
        #         stack.append(self.parseBoolExpr(expression[i]))
        #         i += 1
        #     elif expression[i] in {'!', '&', '|'}:
        #         j, count = i + 2, 1
        #         while j < len(expression) - 1:
        #             if expression[j] == '(':
        #                 count += 1
        #             elif expression[j] == ')':
        #                 count -= 1
        #                 if not count:
        #                     stack.append(self.parseBoolExpr(expression[i:j + 1]))
        #                     i = j + 1
        #                     break
        #             j += 1
        #     else:
        #         i += 1
        # if op == '&':
        #     return all(val for val in stack)
        # return any(val for val in stack)
