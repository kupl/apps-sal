class Solution:

    def maskPII(self, S: str) -> str:
        if '@' in S:
            s = S.split('@')
            s[1] = s[1].split('.')
            s[0] = s[0][0] + '*****' + s[0][-1]
            output = (s[0] + '@' + s[1][0] + '.' + s[1][1]).lower()
        else:
            nums = [i for i in S if i.isdigit()]
            if len(nums) == 10:
                output = f'***-***-{nums[-4]}{nums[-3]}{nums[-2]}{nums[-1]}'
            elif len(nums) == 11:
                output = f'+*-***-***-{nums[-4]}{nums[-3]}{nums[-2]}{nums[-1]}'
            elif len(nums) == 12:
                output = f'+**-***-***-{nums[-4]}{nums[-3]}{nums[-2]}{nums[-1]}'
            else:
                output = f'+***-***-***-{nums[-4]}{nums[-3]}{nums[-2]}{nums[-1]}'
        return output
