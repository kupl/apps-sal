class Solution:

    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = collections.defaultdict(int)
        for i in s:
            d[i] += 1
        zero = '0' * d['z']
        d['e'] -= d['z']
        d['r'] -= d['z']
        d['o'] -= d['z']
        two = '2' * d['w']
        d['t'] -= d['w']
        d['o'] -= d['w']
        four = '4' * d['u']
        d['f'] -= d['u']
        d['o'] -= d['u']
        d['r'] -= d['u']
        five = '5' * d['f']
        d['i'] -= d['f']
        d['v'] -= d['f']
        d['e'] -= d['f']
        six = '6' * d['x']
        d['s'] -= d['x']
        d['i'] -= d['x']
        seven = '7' * d['v']
        d['s'] -= d['v']
        d['e'] -= d['v'] * 2
        d['n'] -= d['v']
        eight = '8' * d['g']
        d['e'] -= d['g']
        d['i'] -= d['g']
        d['h'] -= d['g']
        d['t'] -= d['g']
        nine = '9' * d['i']
        d['n'] -= d['i'] * 2
        d['e'] -= d['i']
        one = '1' * d['o']
        three = '3' * d['r']
        return zero + one + two + three + four + five + six + seven + eight + nine
