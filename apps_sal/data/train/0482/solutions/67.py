class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        table = {}

        def compute(lo, hi):
            if hi - lo == 1:
                return 0

            cost = float('inf')
            for i in range(lo + 1, hi):
                left_key, right_key = f'{lo}-{i}', f'{i}-{hi}'

                if table.get(left_key) is None:
                    table[left_key] = compute(lo, i)
                if table.get(right_key) is None:
                    table[right_key] = compute(i, hi)

                cost = min(cost, table[left_key] + table[right_key] + max(arr[lo: i]) * max(arr[i: hi]))

            return cost

        return compute(0, len(arr))

