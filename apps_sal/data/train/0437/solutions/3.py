class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        fullSize = 0
        for idx, char in enumerate(S):
            if char.isdigit():
                fullSize *=int(char)
            else:
                fullSize+=1
            if fullSize > K:
                break
        endIdx = idx

        for idx in range(endIdx,-1,-1):
            if S[idx].isdigit():
                fullSize /= int(S[idx])
                if K > fullSize:
                    K%=fullSize
            else:
                if K==0 or K == fullSize:
                    return S[idx]
                else:
                    fullSize -=1
