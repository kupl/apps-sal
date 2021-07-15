from collections import deque

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chars = ['a', 'b', 'c']
        queue = deque()
        queue.extend(chars)

        last_length = 0
        length_count = 0
        while len(queue[0]) <= n:
            string = queue.popleft()
            if len(string) != last_length:
                last_length = len(string)
                length_count = 1
            else:
                length_count += 1

            if n == last_length and k == length_count:
                return string

            for char in chars:
                if char != string[-1]:
                    queue.append(string + char)

        return ''

