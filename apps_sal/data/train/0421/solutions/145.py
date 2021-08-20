class Solution:

    def lastSubstring(self, s: str) -> str:
        if not s:
            return ''
        m = s[0]
        for i in range(1, len(s)):
            m = max(m, s[i])
        x = ''
        for i in range(len(s)):
            if s[i] == m:
                x = max(x, s[i:])
        return x
        "\n        if len(x)==1:\n            return s[x[0]:]\n        #print(x)\n        \n        \n        \n        while len(x)>1:\n            c=1\n            m=s[x[0]+c]\n            i=0\n            while i<len(x):\n                #print(x,m)\n                if x[i]+c>=len(s):\n                    if len(x)>1:\n                        x.pop()\n                        break\n                    else:\n                        return s[x[0]:]\n                if s[x[i]+c]<m:\n                    del x[i]\n                    continue\n                if s[x[i]+c]>m:\n                    m=s[x[i]+c]\n                    x=x[i:]\n                    i=0\n                    continue\n                i+=1\n            c+=1\n        if x:\n            return s[x[0]:]\n        \n        return ''\n        "
