class Solution:
    def totalFruit(self, tree) -> int:
        unit_first = tree[0]
        unit_second = -1
        amount_first = 0
        amount_second = 0
        max_amount = 0
        prev = tree[0]
        prev_amount = 0
        for i in range(len(tree)):
            if(tree[i] == prev):
                prev_amount += 1

            if(tree[i] == unit_first):
                amount_first += 1
            elif(tree[i] == unit_second):
                amount_second += 1
            else:
                max_amount = max(max_amount, (amount_first + amount_second))
                unit_first = prev
                amount_first = prev_amount
                unit_second = tree[i]
                amount_second = 1

            if(tree[i] != prev):
                prev_amount = 1

            prev = tree[i]

        return max(max_amount, (amount_first + amount_second))
