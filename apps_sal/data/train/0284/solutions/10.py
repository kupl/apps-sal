class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()

        buyer, seller = 0, len(tokens) - 1
        max_items = current_items = 0

        while buyer <= seller:
            if P >= tokens[buyer]:
                P -= tokens[buyer]
                current_items += 1
                buyer += 1
            else:
                if current_items == 0:
                    break
                else:
                    P += tokens[seller]
                    current_items -= 1
                    seller -= 1
            max_items = max(max_items, current_items)
        return max_items
