class Solution:
    def stoneGameIII(self, cards):
        lookup = {}
        val = self.scoreGivenCards(cards, 0, True, lookup)
        result = val - sum(cards) / 2
        if result > 0:
            return 'Alice'
        elif result < 0:
            return 'Bob'
        else:
            return 'Tie'

    def scoreGivenCards(self, cards, index, is_it_your_turn, lookup):
        if index >= len(cards):
            return 0
        if is_it_your_turn:
            # pick 1
            if (index + 1, not is_it_your_turn) not in lookup:
                lookup[(index + 1, not is_it_your_turn)] = self.scoreGivenCards(cards, index + 1, not is_it_your_turn, lookup)
            score_with_one = cards[index] + lookup[(index + 1, not is_it_your_turn)]
            # pick 2
            if (index + 2, not is_it_your_turn) not in lookup:
                lookup[(index + 2), not is_it_your_turn] = self.scoreGivenCards(cards, index + 2, not is_it_your_turn, lookup)
            score_with_two = sum(cards[index:index + 2]) + lookup[(index + 2, not is_it_your_turn)]
            # pick 3
            if (index + 3, not is_it_your_turn) not in lookup:
                lookup[(index + 3, not is_it_your_turn)] = self.scoreGivenCards(cards, index + 3, not is_it_your_turn, lookup)
            score_with_three = sum(cards[index:index + 3]) + lookup[(index + 3, not is_it_your_turn)]
            return max(score_with_one, score_with_two, score_with_three)
        else:
            # pick 1
            if (index + 1, not is_it_your_turn) not in lookup:
                lookup[(index + 1, not is_it_your_turn)] = self.scoreGivenCards(cards, index + 1, not is_it_your_turn, lookup)
            score_with_one = lookup[(index + 1, not is_it_your_turn)]
            # pick 2
            if (index + 2, not is_it_your_turn) not in lookup:
                lookup[(index + 2, not is_it_your_turn)] = self.scoreGivenCards(cards, index + 2, not is_it_your_turn, lookup)
            score_with_two = lookup[(index + 2, not is_it_your_turn)]
            # pick 3
            if (index + 3, not is_it_your_turn) not in lookup:
                lookup[(index + 3, not is_it_your_turn)] = self.scoreGivenCards(cards, index + 3, not is_it_your_turn, lookup)
            score_with_three = lookup[(index + 3, not is_it_your_turn)]
            return min(score_with_one, score_with_two, score_with_three)
