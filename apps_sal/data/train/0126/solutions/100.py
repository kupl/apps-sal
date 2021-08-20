class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if len(s) < minSize:
            return 0
        if minSize > maxSize:
            return 0
        res = 0
        d = {}
        for i in range(len(s) - minSize + 1):
            temp = s[i:i + minSize]
            if len(set(temp)) <= maxLetters:
                d[temp] = d.get(temp, 0) + 1
                res = max(res, d[temp])
        return res
        '\n        res=0\n        for i in range(minSize,maxSize+1):\n            #print("a")\n            r=[]\n            for j in range(i,len(s)+1):\n                #print(s[j-minSize:j])\n                a=s[j-minSize:j]\n                \n                if len(set(list(a)))<=maxLetters:\n                #print(set(list(a)))\n                    r.append(a)\n            #print(r)\n            if len(r)!=0:\n                r1 = max(set(r), key = r.count) \n            #print(r.count(r1))\n                r2=r.count(r1)\n                res=max(res,r2)\n        return res\n        '
