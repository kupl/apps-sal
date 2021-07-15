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
            K%=fullSize
            if K==0 and S[idx].isalpha():
                return S[idx]
            if S[idx].isdigit():
                fullSize /= int(S[idx])
            else:
                fullSize -=1
