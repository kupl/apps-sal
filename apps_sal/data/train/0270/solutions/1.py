class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        m_vals = 3 * 2 ** (n - 1)
        if k > m_vals:
            return ''
        k -= 1
        m_vals //= 3
        vals = ['a', 'b', 'c']
        mapping = {0: 'a', 1: 'b', 2: 'c'}
        s = mapping[k // m_vals]
        k %= m_vals
        m_vals //= 2
        prev_map = {'a': {0: 'b', 1: 'c'}, 'b': {0: 'a', 1: 'c'}, 'c': {0: 'a', 1: 'b'}}
        while m_vals:
            mapping = prev_map[s[-1]]
            s += mapping[k // m_vals]
            k %= m_vals
            m_vals //= 2
        return s
