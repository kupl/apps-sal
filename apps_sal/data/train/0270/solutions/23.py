class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = [0]
        letters = ['a', 'b', 'c']

        def bt(cur_list=[], last_appended=''):
            if len(cur_list) == n:
                count[0] += 1
                if count[0] == k:
                    return ''.join(cur_list)
                else:
                    return ''
            for i in letters:
                if i == last_appended:
                    continue
                else:
                    cur_list.append(i)
                    output = bt(cur_list, i)
                    if output != '':
                        return output
                    cur_list.pop()
            return ''

        output = bt()
        return '' if not output else output
