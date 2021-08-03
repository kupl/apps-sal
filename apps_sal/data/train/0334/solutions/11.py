'''
1578. Minimum Deletion Cost to Avoid Repeating Letters.  Medium

Given a string items and an array of integers costs where costs[i]
is the costs of deleting the character i in items.

Return the minimum costs of deletions such that there are
no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time,
in other words, after deleting a character, the costs of deleting
other characters will not change.

Example 1:
Input: items = \"abaac\", costs = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter \"a\" with costs 3 to get \"abac\"
             (String without two identical letters next to each other).

Example 2:
Input: items = \"abc\", costs = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because
             there are no identical letters next to each other.

Example 3:
Input: items = \"aabaa\", costs = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character,
             getting the string (\"aba\").

Constraints:
items.length == costs.length
1 <= items.length, costs.length <= 10^5
1 <= costs[i] <= 10^4
items contains only lowercase English letters.

Accepted 3,761 / 7,000 submissions.
'''


class Solution:
    def minCost(self, items: str, costs: List[int]) -> int:
        '''
        Runtime: 1160 ms, faster than 50.00% of Python3 online submissions for Minimum Deletion Cost to Avoid Repeating Letters.
        Memory Usage: 24.5 MB, less than 25.00% of Python3 online submissions for Minimum Deletion Cost to Avoid Repeating Letters.
        '''
        size = len(items)
        if size < 2:
            return 0

        result = 0
        prv_item = items[0]
        prv_cost = costs[0]
        max_cost = tot_cost = prv_cost
        run = False
        for item, cost in zip(items[1:], costs[1:]):
            if item == prv_item:
                run = True
                tot_cost += cost
                max_cost = max(max_cost, cost)
            else:
                if run:
                    run = False
                    result += tot_cost - max_cost
                tot_cost = max_cost = cost
            prv_item = item

        if run:
            result += tot_cost - max_cost
        return result
