class Solution:
    def maskPII(self, S: str) -> str:
        if '@' in S:
            name, domain = S.split('@')
            return name[0].lower() + '*****' + name[-1].lower() + '@' + domain.lower()
        else:
            number = ''
            for c in S:
                if c.isdigit():
                    number += c
            if len(number) == 10:
                return '***-***-' + number[-4:]
            else:
                return '+' + '*' * (len(number) - 10) + '-***-***-' + number[-4:]
