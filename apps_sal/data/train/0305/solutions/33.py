class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        satisfies = set()
        for i in range(2,len(text)+2,2):
            for j in range(0,len(text)-i+1):
                cand = text[j:j+i]
                if cand[:len(cand)//2] == cand[len(cand)//2:]:
                    satisfies.add(cand)
        return len(satisfies)
