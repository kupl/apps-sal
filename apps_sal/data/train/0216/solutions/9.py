class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs)%5!=0 or croakOfFrogs[0]!='c' or croakOfFrogs[-1]!='k':
            return -1

        max_frog_croak = 0
        present_frog_croak = 0

        d={}
        d['c']=0
        d['r']=0
        d['o']=0
        d['a']=0
        d['k']=0

        for ch in croakOfFrogs:
            d[ch]+=1
            if ch=='c':
                present_frog_croak+=1
            if ch=='k':
                present_frog_croak-=1

            max_frog_croak = max(max_frog_croak,present_frog_croak)


        if d['c']!=d['r'] or d['r']!=d['o'] or d['o']!=d['a'] or d['a']!=d['k']:
            return -1

        return max_frog_croak
