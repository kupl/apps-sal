class Solution:
    def parseBoolExpr1(self, expression: str) -> bool:
        def helper(queue):
            res = True
            while queue:
                c = queue.pop()
                print(('c = {0}'.format(c)))
                if c in {'t', 'f'}:
                    return True if c == 't' else False
                if c == '!':
                    queue.pop()
                    res = not helper(queue)
                    queue.pop()
                    return res
                isAnd = True if c == '&' else False
                res = isAnd
                queue.pop()
                while True:
                    if isAnd:
                        res &= helper(queue)
                    else:
                        res |= helper(queue)
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

    def parseBoolExpr(self, expression: str) -> bool:
        def helper(exp, i, j):
            if i == j:
                return exp[i] == 't'
            op = exp[i]
            res = op == '&'
            k, count, prev = i + 1, 0, i + 2
            while k <= j:
                c = exp[k]
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if (count == 1 and c == ',') or not count:
                    val = helper(exp, prev, k - 1)
                    prev = k + 1
                    if op == '!':
                        res = not val
                    elif op == '&':
                        res &= val
                    elif op == '|':
                        res |= val
                k += 1
            return res

        return helper(expression, 0, len(expression) - 1)
