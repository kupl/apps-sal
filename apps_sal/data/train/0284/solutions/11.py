class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        if not len(tokens):
            return 0
        tokens.sort()
        res = 0
        deque = collections.deque(tokens)

        while(len(deque) > 1 and (P >= deque[0] or res)):
            while(deque and P > deque[0]):
                res += 1
                P -= deque.popleft()
            if(len(deque) > 1 and res):
                P += deque.pop()
                res -= 1

        if (deque and P >= deque[0]):
            res += 1
        return res
