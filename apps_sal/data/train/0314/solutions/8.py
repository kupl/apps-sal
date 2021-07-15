class Solution:
    def numSub(self, s: str) -> int:
        self.s = s
        
        modulo = 1000000007

        def numSub(s):
            sOne = ''
            sSub = []
            for i in range(len(s)):
                if s[i] == '1':
                    sOne += '1'
                    if i != len(s) - 1:
                        if s[i + 1] == '1':
                            continue
                        else:
                            sSub.append(sOne)
                            sOne = ''
                    else:
                        sSub.append(sOne)
            return sSub

        sSub = numSub(s)
        num_sOne = 0
        for sOne in sSub:
            len_sOne = len(sOne)
            num_sOne += ((len_sOne * (len_sOne + 1)) // 2) % modulo
        num_sOne %= modulo
        
        return int(num_sOne)
