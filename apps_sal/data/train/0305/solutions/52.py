class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        s=set()
        for j in range(len(text)):
            for i in range(j):
                #print(text[i:j])
                if text[i:j]==text[j:j+j-i]:
                    s.add(text[i:j])
                #print(s)
        return len(s)
