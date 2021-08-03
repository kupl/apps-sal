class Solution:
    def isPossibleDivide(self, hand: List[int], W: int) -> bool:
        if len(hand) % W:
            return False
        cnt = Counter(hand)
        cards = sorted(cnt)
        while True:
            first = cards.pop()
            if not cnt[first]:
                continue
            elif cnt[first] > 1:
                cnt[first] -= 1
                cards.append(first)
            else:
                del cnt[first]
            for i in range(first - 1, first - W, -1):
                if not cnt[i]:
                    return False
                elif cnt[i] > 1:
                    cnt[i] -= 1
                else:
                    del cnt[i]
            if not cnt:
                return True
        return False  # never happen
